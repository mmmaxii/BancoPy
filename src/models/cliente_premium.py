from .cliente import Cliente

# Un cliente premium es un cliente que tiene beneficios adicionales.
# Es un cliente que tiene un saldo minimo y una antiguedad minima.

class ClientePremium(Cliente):
    LIMITE_SALDO = 10000000

    def __init__(self, id, nombre, apellido, rut, email, telefono, 
                 direccion, fecha_registro, saldo, contrasena): 
        
        super().__init__(id, nombre, apellido, rut, email, telefono, 
        direccion, fecha_registro, saldo, contrasena)
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if value > self.LIMITE_SALDO:
            raise ValueError(f"El saldo excede el límite permitido para Cliente Premium (${self.LIMITE_SALDO})")
        
        # lo que hace es llamar al metodo saldo de la clase padre
        # y le pasa el valor que le pasamos
        super(ClientePremium, self.__class__).saldo.fset(self, value)

    def simular_compra_dolares(self, monto_clp: float) -> float:
        tasa_cambio = 950 # Valor dolar simulado
        dolares = monto_clp / tasa_cambio
        return dolares