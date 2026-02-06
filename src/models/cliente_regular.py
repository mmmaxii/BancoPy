from .cliente import Cliente

# Recordar que las variables que tenemos son:

# id, nombre, apellido, email, telefono, _saldo, fecha_registro, estado

# Un cliente regular es un cliente que no tiene ningun beneficio adicional.
# Es el cliente basico.
  
# Antes lo estaba haciendo con *args, **kwargs,
# pero ahora lo hago con parametros nombrados.
class ClienteRegular(Cliente):
    LIMITE_SALDO = 2000000

    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo, contrasena): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value > self.LIMITE_SALDO:
            raise ValueError(f"El saldo excede el límite permitido para Cliente Regular (${self.LIMITE_SALDO})")
        
        # Lo que hace es llamar al metodo saldo de la clase padre
        # y le pasa el valor que le pasamos
        super(ClienteRegular, self.__class__).saldo.fset(self, value)
