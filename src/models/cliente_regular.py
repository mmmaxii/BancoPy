from .cliente import Cliente

# Recordar que las variables que tenemos son:

# id, nombre, apellido, email, telefono, _saldo, fecha_registro, estado

# Un cliente regular es un cliente que no tiene ningun beneficio adicional.
# Es el cliente basico.
  
# Antes lo estaba haciendo con *args, **kwargs,
# pero ahora lo hago con parametros nombrados.
class ClienteRegular(Cliente):
    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
                         direccion, fecha_registro, saldo)


    



