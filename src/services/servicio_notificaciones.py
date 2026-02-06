from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
import os

from models.cliente import Cliente

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")  # ej: miapp.dev@gmail.com

if not SENDGRID_API_KEY:
    raise RuntimeError("SENDGRID_API_KEY no está configurada")

if not FROM_EMAIL:
    raise RuntimeError("FROM_EMAIL no está configurado")


class ServicioNotificaciones:
    def __init__(self):
        self.sg = SendGridAPIClient(SENDGRID_API_KEY)

    def enviar_email_bienvenida(self, cliente: Cliente):
        subject = "Bienvenido/a 🎉"

        html_content = f"""
        <html>
            <body>
                <h1>Bienvenido/a, {cliente.nombre}</h1>
                <p>Gracias por registrarte en nuestra plataforma.</p>
                <p>Esperamos que tengas una excelente experiencia.</p>
            </body>
        </html>
        """

        message = Mail(
            from_email=Email(FROM_EMAIL, "BancoPy"),
            to_emails=To(cliente.email),
            subject=subject,
            html_content=Content("text/html", html_content),
        )

        self._enviar(message)

    def enviar_email_despedida(self, cliente: Cliente):
        subject = "Hasta pronto 👋"

        html_content = f"""
        <html>
            <body>
                <h1>Adiós, {cliente.nombre}</h1>
                <p>Tu cuenta ha sido eliminada correctamente.</p>
                <p>Gracias por haber sido parte de nuestra plataforma.</p>
            </body>
        </html>
        """

        message = Mail(
            from_email=Email(FROM_EMAIL, "BancoPy"),
            to_emails=To(cliente.email),
            subject=subject,
            html_content=Content("text/html", html_content),
        )

        self._enviar(message)

    def _enviar(self, message: Mail):
        try:
            response = self.sg.send(message)
            return response.status_code
        except Exception as e:
            # Aquí solo logueas, NO rompes la app
            print(f"[ERROR] No se pudo enviar email: {e}")
            return None
