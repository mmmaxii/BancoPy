"""
Ya que quiero incorporar un log para las transacciones, me gustaria que el cliente pueda iniciar sesion, 
ver su saldo, sus transacciones y demas. Para eso crearemos la clase LoginCliente que se encargara de:
    
- Ver saldo
- Ver transacciones 
- Hacer depositos 
- Hacer transferencias (Sera entre clientes del banco, pero este debe tener saldo suficiente y el otro cliente debe existir)
- Cerrar sesion (Se guardan todas las transacciones en una database)

cuando se termine salga del login y vuelva al menu principal debemos guardar todo en la base de datos. y volver a
la clase servicio_clientes para que pueda seguir haciendo cosas.
"""

from models.cliente import Cliente

from models.cliente import Cliente
from models.cliente_regular import ClienteRegular
from models.cliente_corporativo import ClienteCorporativo
from models.cliente_premium import ClientePremium
from models.cliente_vip import ClienteVip
from repositorios.repositorio_transacciones import RepositorioTransacciones
from repositorios.repositorio_clientes import RepositorioClientes
from utils.config import PATH_DB_CLIENTES, PATH_DB_TRANSACCIONES

class LoginCliente:
    LIMITE_DIARIO_DEPOSITO = 10000000
    LIMITE_DIARIO_TRANSFERENCIA = 5000000

    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.repo_transacciones = RepositorioTransacciones(PATH_DB_TRANSACCIONES)
        self.repo_clientes = RepositorioClientes(PATH_DB_CLIENTES)

    # clase helper para reconstruir el cliente implementada en la clase servicio_clientes.
    def _reconstruir_cliente_desde_dict(self, datos):
        # Helper simple para reconstruir objeto cliente
        tipo = datos["tipo_cliente"]
        clases = {
            "ClienteRegular": ClienteRegular,
            "ClienteCorporativo": ClienteCorporativo,
            "ClientePremium": ClientePremium,
            "ClienteVip": ClienteVip
        }
        if tipo in clases:
            cliente = clases[tipo](
                id=datos["id"],
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                rut=datos["rut"],
                email=datos["email"],
                telefono=datos["telefono"],
                direccion=datos["direccion"],
                fecha_registro=datos["fecha_registro"],
                saldo=datos["saldo"],
                contrasena=datos["contrasena"]
            )
            cliente.estado = datos["estado"]
            return cliente
        return None
    
    def _verificar_limite_diario(self, tipo_transaccion, monto_nuevo, limite_maximo):
        total_hoy = self.repo_transacciones.calcular_total_diario(self.cliente.id, tipo_transaccion)
        if (total_hoy + monto_nuevo) > limite_maximo:
            raise ValueError(f"La operación excede el límite diario de ${limite_maximo}. Acumulado hoy: ${total_hoy}")

    def ver_saldo(self):
        print(f"Saldo actual: ${self.cliente.saldo}")

    def ver_transacciones(self):
        print("\n--- Historial de Transacciones ---")
        transacciones = self.repo_transacciones.listar_por_cliente(self.cliente.id)
        if not transacciones:
            print("No hay transacciones registradas.")
        else:
            for t in transacciones:
                print(f"[{t['fecha']}] {t['tipo']}: ${t['monto']} - {t['descripcion']}")
            
    def hacer_deposito(self):
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            if monto <= 0:
                print("El monto debe ser positivo.")
                return
            
            # Verificar Limite Diario
            self._verificar_limite_diario("Deposito", monto, self.LIMITE_DIARIO_DEPOSITO)

            # Actualizar objeto
            self.cliente.saldo += monto
            
            # Actualizar BD Clientes
            self.repo_clientes.actualizar_cliente(self.cliente)
            
            # Registrar Transacción
            self.repo_transacciones.guardar_transaccion(
                self.cliente.id, "Deposito", monto, "Deposito en efectivo"
            )
            print(f"Depósito exitoso. Nuevo saldo: ${self.cliente.saldo}")
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error al depositar: {e}")

    def hacer_transferencia(self):
        print("\n--- TRANSFERENCIA DE FONDOS ---")
        rut_destino = input("Ingrese el RUT del destinatario: ")
        
        # 1. Buscar destinatario
        datos_destino = self.repo_clientes.buscar_cliente_por_rut(rut_destino)
        if not datos_destino:
            print("Destinatario no encontrado.")
            return

        destinatario = self._reconstruir_cliente_desde_dict(dict(datos_destino))
        if not destinatario:
            print("Error al procesar datos del destinatario.")
            return
            
        if destinatario.id == self.cliente.id:
            print("No puedes transferirte a ti mismo.")
            return

        print(f"Destinatario: {destinatario.nombre} {destinatario.apellido}")
        
        # 2. Pedir y validar monto
        try:
            monto = float(input("Ingrese monto a transferir: "))
            if monto <= 0:
                print("El monto debe ser positivo.")
                return
            
            if self.cliente.saldo < monto:
                print("Saldo insuficiente.")
                return
            
            # Verificar Limite Diario
            self._verificar_limite_diario("Transferencia Enviada", monto, self.LIMITE_DIARIO_TRANSFERENCIA)
            
            # 3. Ejecutar Transferencia
            # Descontar al origen
            self.cliente.saldo -= monto
            self.repo_clientes.actualizar_cliente(self.cliente)
            
            try:
                # Sumar al destino
                destinatario.saldo += monto
                self.repo_clientes.actualizar_cliente(destinatario)
            except ValueError as e:
                # ROLLBACK: Devolver el dinero al origen si el destino falla
                self.cliente.saldo += monto
                self.repo_clientes.actualizar_cliente(self.cliente)
                print(f"\nError: No se pudo realizar la transferencia al RUT {destinatario.rut}.")
                print("Motivo: El destinatario no puede recibir este monto porque excede su límite de saldo.")
                print(f"Su dinero ha sido devuelto. Saldo actual: ${self.cliente.saldo}")
                return
            
            # 4. Registrar Logs
            # Log para mí (Envío)
            self.repo_transacciones.guardar_transaccion(
                self.cliente.id, 
                "Transferencia Enviada", 
                monto, 
                f"Transferencia a {destinatario.rut}",
                destinatario=destinatario.rut
            )
            
            # Log para el otro (Recepción)
            self.repo_transacciones.guardar_transaccion(
                destinatario.id, 
                "Transferencia Recibida", 
                monto, 
                f"Transferencia de {self.cliente.rut}",
                destinatario=self.cliente.rut
            )
            
            print(f"Transferencia exitosa. Tu nuevo saldo: ${self.cliente.saldo}")
            
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error en la transacción: {e}")

    def cerrar_sesion(self):
        print("Cerrando sesión...")
        self.repo_clientes.cerrar_conexion()

    def acceder_servicios_especiales(self):
        print(f"\n--- SERVICIOS ESPECIALES: {self.cliente.__class__.__name__} ---")
        
        if isinstance(self.cliente, ClienteRegular):
            print("SIMULADOR DE DEPÓSITO A PLAZO")
            try:
                monto = float(input("Monto a invertir: "))
                dias = int(input("Días plazo: "))
                ganancia = self.cliente.simular_cdp(monto, dias)
                print(f"Ganancia estimada: ${ganancia:.2f}")
            except ValueError:
                print("Datos inválidos.")

        elif isinstance(self.cliente, ClientePremium):
            print("SIMULADOR COMPRA DÓLARES")
            try:
                monto = float(input("Monto en CLP a cambiar: "))
                dolares = self.cliente.simular_compra_dolares(monto)
                print(f"Recibirías: US${dolares:.2f}")
            except ValueError:
                print("Monto inválido.")

        elif isinstance(self.cliente, ClienteVip):
            print("PORTAFOLIO DE INVERSIÓN")
            mensaje = self.cliente.abrir_portafolio_inversion()
            print(mensaje)

        elif isinstance(self.cliente, ClienteCorporativo):
            print("CÁLCULO DE NÓMINA")
            try:
                empleados = int(input("Número de empleados: "))
                promedio = float(input("Sueldo promedio: "))
                total = self.cliente.calcular_nomina_sueldos(empleados, promedio)
                print(f"Total a provisionar (con 3% costos): ${total:.2f}")
            except ValueError:
                print("Datos inválidos.")