# umbrella_report_weekly.py

import os
import requests
import pandas as pd
import schedule
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import pytz
from email.message import EmailMessage
import smtplib
import logging

# Configuración de logging
logging.basicConfig(
    filename="umbrella_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("UMBRELLA_REPORT_API_KEY")
ORG_ID = os.getenv("UMBRELLA_ORG_ID")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

# Validar que todas las variables necesarias estén definidas
required_vars = {
    "UMBRELLA_REPORT_API_KEY": API_KEY,
    "UMBRELLA_ORG_ID": ORG_ID,
    "EMAIL_FROM": EMAIL_FROM,
    "EMAIL_PASSWORD": EMAIL_PASSWORD,
    "EMAIL_TO": EMAIL_TO,
}

missing_vars = [var for var, value in required_vars.items() if not value]
if missing_vars:
    raise EnvironmentError(f"🚨 Faltan variables en el archivo .env: {', '.join(missing_vars)}")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_dns_activity():
    tz = pytz.timezone("America/Mexico_City")
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(days=7)

    logging.info(f"📥 Extrayendo datos de {start_time.isoformat()} a {end_time.isoformat()}...")

    url = f"https://reports.api.umbrella.com/v2/organizations/{ORG_ID}/activity/dns"
    offset = 0
    all_data = []

    while True:
        params = {
            "start": start_time.isoformat(),
            "end": end_time.isoformat(),
            "limit": 1000,
            "offset": offset
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Error al conectar con la API: {e}")
            return

        data = response.json().get("data", [])
        if not data:
            break

        all_data.extend(data)
        offset += len(data)

    if not all_data:
        logging.warning("⚠️ No se encontraron registros para esta semana.")
        return

    df = pd.DataFrame(all_data)
    filename = f"umbrella_dns_report_{end_time.strftime('%Y-%m-%d')}.xlsx"
    df.to_excel(filename, index=False)
    logging.info(f"✅ Reporte guardado como {filename}")

    send_email(filename)

def send_email(attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "Reporte semanal de Cisco Umbrella"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content("Adjunto encontrarás el reporte semanal de actividad DNS.")

    try:
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
    except Exception as e:
        logging.error(f"❌ Error al leer el archivo adjunto: {e}")
        return

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            smtp.send_message(msg)
        logging.info(f"📧 Correo enviado con éxito a {EMAIL_TO}")
    except Exception as e:
        logging.error(f"❌ Error al enviar el correo: {e}")

# Programar ejecución automática cada lunes a las 08:00 (CDMX)
schedule.every().monday.at("08:00").do(fetch_dns_activity)

logging.info("⏱ Script iniciado. Esperando el lunes a las 08:00 (CDMX)...")

while True:
    schedule.run_pending()
    time.sleep(60)
