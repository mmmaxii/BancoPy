from .cliente import Cliente

# Recordar que las variables que tenemos son:

# id, nombre, apellido, email, telefono, _saldo, fecha_registro, estado

# Un cliente regular es un cliente que no tiene ningun beneficio adicional.
# Es el cliente basico.

class ClienteRegular(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


