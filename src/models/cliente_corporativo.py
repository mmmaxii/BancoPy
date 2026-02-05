from .cliente import Cliente

class ClienteCorporativo(Cliente):
    def __init__(self, id, nombre, apellido, email, telefono, 
                 direccion, fecha_registro, estado, saldo): 
        
        super().__init__(id, nombre, apellido, email, telefono, 
                         direccion, fecha_registro, estado, saldo)