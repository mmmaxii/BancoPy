from .cliente import Cliente

# Un cliente premium es un cliente que tiene beneficios adicionales.
# Es un cliente que tiene un saldo minimo y una antiguedad minima.

class ClientePremium(Cliente):
    def __init__(self, id, nombre, apellido, email, telefono, 
                 direccion, fecha_registro, saldo): 
        
        super().__init__(id, nombre, apellido, email, telefono, 
                         direccion, fecha_registro, saldo)