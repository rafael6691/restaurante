import smtplib
from email.mime.text import MIMEText
import os

# Configuración de SMTP (editar según tu proveedor)
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'tu_email@example.com'
SMTP_PASS = 'tu_contraseña'

def enviar_confirmacion(email_destino, asunto, mensaje):
    msg = MIMEText(mensaje, 'plain')
    msg['Subject'] = asunto
    msg['From'] = SMTP_USER
    msg['To'] = email_destino

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
