from .cliente import Cliente

# Quizas una buena opcion para cliente VIP es no tener un limite de retiro diario
# Un cliente puede directamente acceder a este "plan" sin pasar por el proceso de 
# antiguedad o de tener un saldo minimo.
# Por eso mismo debe pagar una membresia mensual.

class ClienteVip(Cliente):
    LIMITE_SALDO = 50000000

    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo, contrasena): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value > self.LIMITE_SALDO:
            raise ValueError(f"El saldo excede el límite permitido para Cliente VIP (${self.LIMITE_SALDO})")ç
        # lo que hace es llamar al metodo saldo de la clase padre
        # y le pasa el valor que le pasamos
        super(ClienteVip, self.__class__).saldo.fset(self, value)


