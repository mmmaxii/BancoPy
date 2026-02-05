# TODO: Implementar lógica de validación (local + API externa)

# Lo mismo que hice para el caso de las notificaciones, voy a usar una clase
# para esto, la cual se encargara de validar los datos de los clientes.

class ServicioValidacionEmailApi:
    def __init__(self):
        pass

    # Solo voy a validar el email, ya que es el unico dato que se puede validar con una API externa.
    # Quizas es posible validar el telefono con una API externa, pero no estoy seguro de implementarlo.
    # Por ahora solo validare el email.
    def validar_email(self, email: str):
        pass
    

