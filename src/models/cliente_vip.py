from .cliente import Cliente

# Quizas una buena opcion para cliente VIP es no tener un limite de retiro diario
# Un cliente puede directamente acceder a este "plan" sin pasar por el proceso de 
# antiguedad o de tener un saldo minimo.
# Por eso mismo debe pagar una membresia mensual.

class ClienteVip(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


