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

# Cargar variables del entorno (.env)
load_dotenv()

API_KEY = os.getenv("UMBRELLA_REPORT_API_KEY")
ORG_ID = os.getenv("UMBRELLA_ORG_ID")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def fetch_dns_activity():
    tz = pytz.timezone("America/Mexico_City")
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(days=7)

    print(f"📥 Extrayendo datos de {start_time.date()} a {end_time.date()}...")

    url = f"https://reports.api.umbrella.com/v2/organizations/{ORG_ID}/activity/dns"
    params = {
        "start": start_time.isoformat(),
        "end": end_time.isoformat(),
        "limit": 1000  # Puedes paginar si necesitas más
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", [])
        if not data:
            print("⚠️ No se encontraron registros para esta semana.")
            return

        df = pd.DataFrame(data)
        filename = f"umbrella_dns_report_{end_time.strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(filename, index=False)
        print(f"✅ Reporte guardado como {filename}")

        send_email(filename)
    else:
        print("❌ Error en API:", response.status_code, response.text)

def send_email(attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "Reporte semanal de Cisco Umbrella"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content("Adjunto encontrarás el reporte semanal de actividad DNS.")

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("📧 Correo enviado con éxito a", EMAIL_TO)

# Programar ejecución automática
schedule.every().monday.at("08:00").do(fetch_dns_activity)

print("⏱ Esperando el lunes a las 08:00 (CDMX)...")

while True:
    schedule.run_pending()
    time.sleep(60)
