from .cliente import Cliente

# Un cliente premium es un cliente que tiene beneficios adicionales.
# Es un cliente que tiene un saldo minimo y una antiguedad minima.

class ClientePremium(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
