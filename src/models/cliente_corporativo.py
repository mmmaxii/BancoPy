from .cliente import Cliente

class ClienteCorporativo(Cliente):
    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
                         direccion, fecha_registro, saldo)