"""
Este archivo contiene la clase ServicioClientes que sera el
cerebro de todo. 
"""

from utils.inputs_usuario import InputsUsuario as I_U
from repositorios.repositorio_clientes import RepositorioClientes
from models.cliente_regular import ClienteRegular
from models.cliente_corporativo import ClienteCorporativo
from models.cliente_premium import ClientePremium
from models.cliente_vip import ClienteVip
from utils.config import PATH_DB_CLIENTES, PATH_DB_CLIENTES, PATH_DB_TRANSACCIONES
from pathlib import Path
from .servicio_notificaciones import ServicioNotificaciones

# Lo que quiero hacer con esta funcion es organizar todas las funciones que tenemos


# Primero lo primero, agregar un nuevo cliente (funcion agregar_cliente)
# 1. Pedir los inputs para crear un nuevo cliente
# 2. Verificar errores de formato con ValidadorFormato (Clase)
# 3. Luego verificamos si el gmail existe con ServicioValidacionEmailApi (Clase)
# 4. Si todo esta bien, creamos el cliente y enviamos una notificacion con ServicioNotificaciones (Clase)

class ServicioClientes:
    def __init__(self):
        pass
    
    # Primero solo validaremos y mas adelante agregamos la validacion de email real
    # junto con las notificaciones
    def agregar_cliente(self):
        id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena, tipo_cliente = I_U().pedir_inputs_nuevo_cliente()
        
        cliente = None
        if tipo_cliente == "ClienteRegular":
            cliente = ClienteRegular(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        elif tipo_cliente == "ClientePremium":
            cliente = ClientePremium(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        elif tipo_cliente == "ClienteVip":
            cliente = ClienteVip(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        elif tipo_cliente == "ClienteCorporativo":
            cliente = ClienteCorporativo(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        
        print(f"Cliente {cliente.nombre} creado exitosamente con estado: {cliente.estado}")
        
    
        if RepositorioClientes(PATH_DB_CLIENTES).guardar_cliente(cliente):
            print("Cliente guardado exitosamente en la base de datos")

            ServicioNotificaciones().enviar_email_bienvenida(cliente)
            print("Correo de bienvenida enviado exitosamente")
    
    def ver_todos_los_clientes(self):
        clientes = RepositorioClientes(PATH_DB_CLIENTES).listar_clientes()

        confirmacion = input("\nIngrese contraseña de administrador para confirmar: ")
        
        if confirmacion == "admin1234":
            if not clientes:
                print("No hay clientes en la base de datos")
            
            # Mejora visual para que se vea mas ordenadoq
            print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
            for cliente_data in clientes:
                cliente_obj = self._reconstruir_cliente(cliente_data)
                if cliente_obj:
                    print(f"ID: {cliente_obj.id} | {cliente_obj} | RUT: {cliente_obj.rut} | Email: {cliente_obj.email} | Contraseña: {cliente_obj.contrasena}")
                else:
                    # Fallback si falla la reconstrucción
                    print(dict(cliente_data))
        else:
            print("Contraseña incorrecta. Operación cancelada.")
        
        
    def _reconstruir_cliente(self, cliente_data):
        """Método helper para reconstruir un objeto Cliente desde los datos de la BD."""
        # Se tiene que pasar a dict para que funcione el metodo, ya que 
        # el repositorio devuelve un objeto de tipo Row
        cliente_data = dict(cliente_data)
        tipo = cliente_data["tipo_cliente"]
        
        clases = {
            "ClienteRegular": ClienteRegular,
            "ClienteCorporativo": ClienteCorporativo,
            "ClientePremium": ClientePremium,
            "ClienteVip": ClienteVip
        }
        
        if tipo in clases:
            cliente_obj = clases[tipo](
                id=cliente_data["id"],
                nombre=cliente_data["nombre"],
                apellido=cliente_data["apellido"],
                rut=cliente_data["rut"],
                email=cliente_data["email"],
                telefono=cliente_data["telefono"],
                direccion=cliente_data["direccion"],
                fecha_registro=cliente_data["fecha_registro"],
                saldo=cliente_data["saldo"],
                contrasena=cliente_data["contrasena"]
            )
            cliente_obj.estado = cliente_data["estado"]
            return cliente_obj
        return None

    def iniciar_sesion(self):
        identificador, contrasena = I_U().pedir_credenciales_login()
        
        repo = RepositorioClientes(PATH_DB_CLIENTES)

        cliente_data = None
        
        if "@" in identificador:
            cliente_data = repo.buscar_cliente_por_email(identificador)
        else:
            cliente_data = repo.buscar_cliente_por_rut(identificador)
            
        if not cliente_data:
            print("Usuario no encontrado.")
            return None

        print(cliente_data)            
        if cliente_data["contrasena"] != contrasena:
            print("Contraseña incorrecta.")
            return None
            
        cliente_obj = self._reconstruir_cliente(cliente_data)
        
        if cliente_obj:
            print(f"Bienvenido/a {cliente_obj.nombre} {cliente_obj.apellido}!")
            return cliente_obj
        else:
            print(f"Error: Tipo de cliente desconocido '{cliente_data['tipo_cliente']}'.")
            return None

    def eliminar_cliente_admin(self):
        print("\n--- ELIMINAR CLIENTE (MODO ADMIN) ---")
        identificador = input("Ingrese RUT o Email del cliente a eliminar: ")
        
        repo = RepositorioClientes(PATH_DB_CLIENTES)
        cliente_data = None
        
        if "@" in identificador:
            cliente_data = repo.buscar_cliente_por_email(identificador)
        else:
            cliente_data = repo.buscar_cliente_por_rut(identificador)
            
        if not cliente_data:
            print("Cliente no encontrado.")
            return

        cliente = self._reconstruir_cliente(cliente_data)

        if not cliente:
            print("Error al reconstruir cliente.")
            return

        print("\nDatos del cliente a eliminar:")
        print(cliente) # Usa el __str__ modificado
        
        confirmacion = input("\nIngrese contraseña de administrador para confirmar: ")
        
        if confirmacion == "admin1234":
            ServicioNotificaciones().enviar_email_despedida(cliente)
            print(f"Cliente {cliente.nombre} {cliente.apellido} eliminado exitosamente.")
            repo.eliminar_cliente(cliente)
        else:
            print("Contraseña incorrecta. Operación cancelada.")
        
    
    
    