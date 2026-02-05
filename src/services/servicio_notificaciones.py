from ..models.cliente import Cliente

# Implementar lógica de notificaciones (API de Email)
# Ya me decidi usar una clase para esto, la cual se encargara de enviar notificaciones
# a los clientes

from dotenv import load_dotenv
import os

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

if not SENDGRID_API_KEY:
    raise RuntimeError("SENDGRID_API_KEY no está configurada")




class ServicioNotificaciones:
    def __init__(self):
        pass

    # Me parece prudente solo agregar estas dos opciones ya que la API que encontre solo me deja
    # enviar 500 emails al mes.

    def enviar_email_bienvenida(self, cliente: Cliente):
        pass
    
    def enviar_email_despedida(self, cliente: Cliente):
        pass
