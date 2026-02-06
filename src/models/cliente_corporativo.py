from .cliente import Cliente

class ClienteCorporativo(Cliente):
    LIMITE_SALDO = 100000000

    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo, contrasena): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value > self.LIMITE_SALDO:
            raise ValueError(f"El saldo excede el límite permitido para Cliente Corporativo (${self.LIMITE_SALDO})")
        
        # lo que hace es llamar al metodo saldo de la clase padre
        # y le pasa el valor que le pasamos
        super(ClienteCorporativo, self.__class__).saldo.fset(self, value)