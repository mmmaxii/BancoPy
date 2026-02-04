from ..models.cliente import Cliente
# Implementar lógica de notificaciones (API de Email)
# Ya me decidi usar una clase para esto, la cual se encargara de enviar notificaciones
# a los clientes


class ServicioNotificaciones:
    def __init__(self):
        pass

    # Me parece prudente solo agregar estas dos opciones ya que la API que encontre solo me deja
    # enviar 500 emails al mes.

    def enviar_email_bienvenida(self, cliente: Cliente):
        pass
    
    def enviar_email_despedida(self, cliente: Cliente):
        pass
