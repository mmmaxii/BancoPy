# Clases para los tipos de clientes
from .cliente import Cliente

# Recordar que las variables que tenemos son:

# id, nombre, apellido, email, telefono, saldo, fecha_registro, estado

class ClienteRegular(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ClientePremium(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Quizas una buena opcion para cliente VIP es no tener un limite de retiro diario
# Un cliente puede directamente acceder a este "plan" sin pasar por el proceso de 
# antiguedad o de tener un saldo minimo.
# Por eso mismo debe pagar una membresia mensual.

class ClienteVip(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ClienteCorporativo(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
