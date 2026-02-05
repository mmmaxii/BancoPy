from .cliente import Cliente

# Recordar que las variables que tenemos son:

# id, nombre, apellido, email, telefono, _saldo, fecha_registro, estado

# Un cliente regular es un cliente que no tiene ningun beneficio adicional.
# Es el cliente basico.

class ClienteRegular(Cliente):
    def __init__(self, id, nombre, apellido, email, telefono, 
                 direccion, fecha_registro, estado, saldo, 
                 beneficio_cafeteria: bool): 
        
        # Antes lo estaba haciendo con *args, **kwargs,
        # pero ahora lo hago con parametros nombrados.
        super().__init__(id, nombre, apellido, email, telefono, 
                         direccion, fecha_registro, estado, saldo)
        

        self.beneficio_cafeteria = beneficio_cafeteria

    
    


