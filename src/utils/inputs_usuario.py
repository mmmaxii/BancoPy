from .validadores_de_formato import ValidadorFormato as V_F
from .generador_rut import generar_rut
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
        
        # Lógica de RUT con Generador
        rut_input = input("Ingrese el RUT (o escriba 'generar' para uno aleatorio): ")
        if rut_input.lower().strip() == "generar":
            rut = generar_rut()
            print(f"RUT Generado: {rut}")
        else:
            rut = rut_input
            V_F.validar_rut(rut)
        email = input("Ingrese el email del cliente: ")
        V_F.validar_email(email)
        telefono = input("Ingrese el telefono del cliente: ")
        V_F.validar_telefono(telefono)
        direccion = input("Ingrese la direccion del cliente: ")
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # estado = "Activo" # Ya no pedimos estado, se setea solo en el __init__
        saldo = float(input("Ingrese el saldo inicial: "))
        contrasena = input("Ingrese una contraseña segura: ")
        
        print("\nSeleccione el tipo de cuenta:")
        print("1. Cliente Regular")
        print("2. Cliente Premium")
        print("3. Cliente VIP")
        print("4. Cliente Corporativo")
        opcion_tipo = input("Opción: ")
        
        tipo_cliente = "ClienteRegular" # Default
        if opcion_tipo == "1":
            tipo_cliente = "ClienteRegular"
        elif opcion_tipo == "2":
            tipo_cliente = "ClientePremium"
        elif opcion_tipo == "3":
            tipo_cliente = "ClienteVip"
        elif opcion_tipo == "4":
            tipo_cliente = "ClienteCorporativo"
        
        return id, nombre, apellido, rut, email, telefono, direccion, fecha_registro, saldo, contrasena, tipo_cliente

    def pedir_credenciales_login(self):
        identificador = input("Ingrese su RUT o Email: ")
        contrasena = input("Ingrese su contraseña: ")
        return identificador, contrasena