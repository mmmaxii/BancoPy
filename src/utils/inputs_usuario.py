from .validadores_de_formato import ValidadorFormato as V_F
from datetime import datetime

class InputsUsuario:
    def __init__(self):
        pass

    def pedir_inputs_nuevo_cliente(self):
        # Tiene que pedir todos los parametros de la clase cliente
        # Y ademas tiene que validar que los datos sean correctos
        # Usando la clase ValidadorFormato
        id = None 
        nombre = input("Ingrese el nombre del cliente: ")
        # Si nos damos cuenta, no instanciamos la clase, sino que simplemente
        # usamos el metodo estatico (@staticmethod). 
        V_F.validar_nombre(nombre)
        apellido = input("Ingrese el apellido del cliente: ")
        V_F.validar_nombre(apellido)
        rut = input("Ingrese el RUT del cliente (ej: 12345678-9): ")
        V_F.validar_rut(rut)
        email = input("Ingrese el email del cliente: ")
        V_F.validar_email(email)
        telefono = input("Ingrese el telefono del cliente: ")
        V_F.validar_telefono(telefono)
        direccion = input("Ingrese la direccion del cliente: ")
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # estado = "Activo" # Ya no pedimos estado, se setea solo en el __init__
        saldo = float(input("Ingrese el saldo del cliente: "))
        contrasena = input("Ingrese una contraseña segura: ")
        tipo_cliente = input("Ingrese el tipo de cliente (Persona/Empresa): ")
        
        return id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena, tipo_cliente

    def pedir_credenciales_login(self):
        identificador = input("Ingrese su RUT o Email: ")
        contrasena = input("Ingrese su contraseña: ")
        return identificador, contrasena