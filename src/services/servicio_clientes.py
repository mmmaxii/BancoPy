"""
Este archivo contiene la clase ServicioClientes que sera el
cerebro de todo. 
"""

from utils.inputs_usuario import InputsUsuario as I_U
from repositorios.repositorio_clientes import RepositorioClientes
from models.cliente_regular import ClienteRegular
from models.cliente_corporativo import ClienteCorporativo
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
        id, nombre, apellido, email, telefono, direccion, fecha_registro, saldo, tipo_cliente = I_U().pedir_inputs_nuevo_cliente()
        
        cliente = None
        if tipo_cliente == "Persona":
            cliente = ClienteRegular(id, nombre, apellido, email, telefono, direccion, fecha_registro, saldo)
        elif tipo_cliente == "Empresa":
            cliente = ClienteCorporativo(id, nombre, apellido, email, telefono, direccion, fecha_registro, saldo)
        
        # Guardar en repositorio (si lo has instanciado)
        # self.repositorio.guardar_cliente(cliente)
        print(f"Cliente {cliente.nombre} creado exitosamente con estado: {cliente.estado}")
        
        
    