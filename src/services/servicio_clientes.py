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
from utils.config import PATH_DB_TEST
from pathlib import Path

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
        if tipo_cliente == "Persona":
            cliente = ClienteRegular(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        elif tipo_cliente == "Empresa":
            cliente = ClienteCorporativo(id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena)
        
        # Guardar en repositorio (si lo has instanciado)
        # self.repositorio.guardar_cliente(cliente)
        print(f"Cliente {cliente.nombre} creado exitosamente con estado: {cliente.estado}")
        
        RepositorioClientes(PATH_DB_TEST).guardar_cliente(cliente)
        print("Cliente guardado exitosamente en la base de datos")

    
    def ver_todos_los_clientes(self):
        clientes = RepositorioClientes(PATH_DB_TEST).listar_clientes()
        for cliente in clientes:
            print(dict(cliente))
        
    def iniciar_sesion(self):
        identificador, contrasena = I_U().pedir_credenciales_login()
        
        repo = RepositorioClientes(PATH_DB_TEST)
        cliente_data = None
        
        # Determinar si es RUT o Email (simple check: si tiene @ es email)
        if "@" in identificador:
            cliente_data = repo.buscar_cliente_por_email(identificador)
        else:
            cliente_data = repo.buscar_cliente_por_rut(identificador)
            
        if not cliente_data:
            print("Usuario no encontrado.")
            return None
            
        # Validar contraseña
        if cliente_data["contrasena"] != contrasena:
            print("Contraseña incorrecta.")
            return None
            
        # Reconstruir el objeto según el tipo de cliente
        tipo = cliente_data["tipo_cliente"]
        
        # Diccionario para instanciar la clase correcta
        clases = {
            "ClienteRegular": ClienteRegular,
            "ClienteCorporativo": ClienteCorporativo,
            "ClientePremium": ClientePremium,
            "ClienteVip": ClienteVip
        }
        
        if tipo in clases:
            # Extraemos los argumentos necesarios para el constructor
            # Nota: El constructor espera: id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena
            # El row_factory de sqlite3 devuelve algo parecido a un dict
            
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
            # Aseguramos el estado
            cliente_obj.estado = cliente_data["estado"]
            
            print(f"Bienvenido/a {cliente_obj.nombre} {cliente_obj.apellido}!")
            return cliente_obj
        else:
            print(f"Error: Tipo de cliente desconocido '{tipo}'.")
            return None
        
        
    