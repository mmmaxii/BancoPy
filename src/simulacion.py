from repositorios.repositorio_clientes import RepositorioClientes
from repositorios.repositorio_transacciones import RepositorioTransacciones
from services.servicio_login_cliente import LoginCliente
from models.cliente_regular import ClienteRegular
from models.cliente_premium import ClientePremium
from utils.config import PATH_DB_CLIENTES, PATH_DB_TRANSACCIONES
from utils.generador_rut import generar_rut
from datetime import datetime
import random

def correr_simulacion():
    print("=== INICIO DE SIMULACIÓN BANCARIA (Arquitectura Real) ===\n")

    # 1. Preparar Repositorios
    repo_clientes = RepositorioClientes(PATH_DB_CLIENTES)
    repo_transacciones = RepositorioTransacciones(PATH_DB_TRANSACCIONES)

    # 2. Crear Clientes (Objetos)
    rut1 = generar_rut()
    rut2 = generar_rut()
    
    print(f"[Simulación] Creando clientes ficticios:")
    print(f" - Cliente 1 (Regular): RUT {rut1}")
    print(f" - Cliente 2 (Premium): RUT {rut2}")

    c1 = ClienteRegular(
        id=None, 
        nombre="Ana", 
        apellido="Simulada", 
        rut=rut1, 
        email=f"ana.{random.randint(1000,9999)}@test.com", 
        telefono="555-1111", 
        direccion="Calle Falsa 123", 
        fecha_registro=str(datetime.now()), 
        saldo=500000.0, 
        contrasena="1234"
    )

    c2 = ClientePremium(
        id=None, 
        nombre="Beto", 
        apellido="Tester", 
        rut=rut2, 
        email=f"beto.{random.randint(1000,9999)}@test.com", 
        telefono="555-2222", 
        direccion="Av. Siempre Viva 742", 
        fecha_registro=str(datetime.now()), 
        saldo=1000000.0, 
        contrasena="1234"
    )

    # 3. Registrar en Base de Datos
    # Al guardar, c1.id y c2.id se actualizan automáticamente con el ID de la BD
    repo_clientes.guardar_cliente(c1)
    repo_clientes.guardar_cliente(c2)
    print("\n[Simulación] Clientes guardados en base de datos SQLite.")
    print(f" - ID Ana: {c1.id}")
    print(f" - ID Beto: {c2.id}")

    # 4. Simular Operación Bancaria (Transferencia)
    sesion_ana = LoginCliente(c1)
    
    print(f"\n[Simulación] {c1.nombre} ha iniciado sesión para transferir.")
    print(f"Saldo Inicial de Ana: ${c1.saldo:,.0f}")

    try:
        monto_transferencia = 200000.0
        print(f"Intentando transferir ${monto_transferencia:,.0f} a {c2.nombre}...")

        if sesion_ana.cliente.saldo >= monto_transferencia:
            # --- Lógica de Negocio ---
            
            # 1. Actualizar Saldos en Memoria
            sesion_ana.cliente.saldo -= monto_transferencia
            c2.saldo += monto_transferencia
            
            # 2. Persistir Saldos en BD Clientes
            repo_clientes.actualizar_cliente(sesion_ana.cliente)
            repo_clientes.actualizar_cliente(c2)
            
            print("[Simulación] ¡Saldos actualizados!")
            print(f"Nuevo Saldo Ana:  ${sesion_ana.cliente.saldo:,.0f}")
            print(f"Nuevo Saldo Beto: ${c2.saldo:,.0f}")
            
            # 3. Registrar Transacciones (Historial)
            # Log para Ana (Envío)
            repo_transacciones.guardar_transaccion(
                cliente_id=c1.id,
                tipo="Transferencia Enviada",
                monto=monto_transferencia,
                descripcion=f"Transferencia a {c2.rut}",
                destinatario=c2.rut
            )
            
            # Log para Beto (Recepción)
            repo_transacciones.guardar_transaccion(
                cliente_id=c2.id,
                tipo="Transferencia Recibida",
                monto=monto_transferencia,
                descripcion=f"Transferencia de {c1.rut}",
                destinatario=c1.rut
            )
            
            print("[Simulación] Transacciones registradas en el historial.")
            
    except Exception as e:
        print(f"[Error] {e}")

    print("\n=== FIN DE SIMULACIÓN ===")

if __name__ == "__main__":
    correr_simulacion()
