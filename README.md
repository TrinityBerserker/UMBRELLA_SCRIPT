# 🛡️ Umbrella DNS Report - Automatización Semanal

Este proyecto automatiza la descarga y reporte de datos DNS de Cisco Umbrella, generando reportes semanales en formato Excel y enviándolos por correo electrónico.

## ✅ ¿Qué hace este proyecto?

Cada lunes a las 08:00 (hora de Ciudad de México):

- Se conecta a Cisco Umbrella
- Descarga los datos completos de actividad DNS de los últimos 7 días
- Genera un archivo Excel (.xlsx) con el nombre `umbrella_dns_report_YYYY-MM-DD.xlsx`
- (Opcional) Envía ese archivo por correo automáticamente

## 📨 Cómo funciona el envío por correo (SMTP)

El script usa el protocolo SMTP para enviar un correo con el archivo Excel adjunto. Esto requiere:

### 🔐 Un correo emisor

Un correo tipo Gmail, Outlook, corporativo, etc., con los siguientes datos:

| Dato necesario | Ejemplo |
|---|---|
| Correo emisor | reportes@tudominio.com |
| Contraseña o token | contraseñaSMTP o App Password |
| Correo destinatario | ciberseguridad@empresa.com |

### ⚠️ Gmail requiere activar "App Passwords"

Si usas Gmail, debes activar la verificación en dos pasos y generar una contraseña de aplicación.
[Guía oficial de Google](https://support.google.com/accounts/answer/185833)

## 📁 Estructura de archivos

```
/umbrella_report/
│
├── .env                <- Datos sensibles (API y correo)
├── umbrella_report_weekly.py
├── requirements.txt
└── dist/               <- Aquí quedará tu ejecutable (.exe)
```

## 📄 Contenido del archivo .env (ejemplo)

```env
UMBRELLA_REPORT_API_KEY=tu_token_api
UMBRELLA_ORG_ID=tu_org_id
EMAIL_FROM=correo@gmail.com
EMAIL_PASSWORD=clave_o_token
EMAIL_TO=destinatario@empresa.com
```

## 🖥️ Cómo generar el ejecutable .exe

1. Asegúrate de tener Python instalado

2. Instala pyinstaller:
   ```bash
   pip install pyinstaller
   ```

3. Desde la carpeta del script:
   ```bash
   pyinstaller --onefile umbrella_report_weekly.py
   ```

Esto generará en `/dist/umbrella_report_weekly.exe` un ejecutable listo para correr en cualquier máquina Windows.

## 🚀 Instalación y configuración

### Requisitos previos
- Python 3.7+
- Acceso a la API de Cisco Umbrella
- (Opcional) Cuenta de correo con acceso SMTP

### Pasos de instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/umbrella-dns-report.git
   cd umbrella-dns-report
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno:**
   - Copia el archivo `.env.example` a `.env`
   - Completa los datos de tu API de Umbrella y configuración SMTP

4. **Ejecuta el script:**
   ```bash
   python umbrella_report_weekly.py
   ```

## 📊 Características del reporte

- **Formato:** Excel (.xlsx)
- **Contenido:** Actividad DNS completa de los últimos 7 días
- **Nomenclatura:** `umbrella_dns_report_YYYY-MM-DD.xlsx`
- **Programación:** Lunes a las 08:00 (GMT-6)

## 🔧 Personalización

Puedes modificar los siguientes aspectos en el script:

- **Horario de ejecución:** Cambia la programación en el código
- **Período de datos:** Ajusta el rango de días para el reporte
- **Destinatarios:** Añade múltiples correos de destino
- **Formato:** Personaliza el contenido del Excel

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Si tienes problemas o preguntas, por favor abre un issue en GitHub o contacta al equipo de desarrollo.

---

⚡ **Automatiza tu monitoreo DNS con Cisco Umbrella**
