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



# 📚 Librerías Necesarias

Este proyecto requiere las siguientes librerías de Python para funcionar correctamente:

## 📦 Lista de dependencias

```
requests
pandas
openpyxl
schedule
pytz
python-dotenv
```

## 📋 Descripción de cada librería

### 🌐 requests
- **Propósito**: Realizar peticiones HTTP a la API de Cisco Umbrella
- **Uso**: Descargar datos DNS y comunicarse con servicios web
- **Documentación**: [requests.readthedocs.io](https://requests.readthedocs.io)

### 📊 pandas
- **Propósito**: Manipulación y análisis de datos
- **Uso**: Procesar los datos DNS descargados y estructurarlos
- **Documentación**: [pandas.pydata.org](https://pandas.pydata.org)

### 📈 openpyxl
- **Propósito**: Crear y manipular archivos Excel (.xlsx)
- **Uso**: Generar los reportes en formato Excel
- **Documentación**: [openpyxl.readthedocs.io](https://openpyxl.readthedocs.io)

### ⏰ schedule
- **Propósito**: Programar tareas automáticas
- **Uso**: Ejecutar el script cada lunes a las 08:00
- **Documentación**: [schedule.readthedocs.io](https://schedule.readthedocs.io)

### 🌍 pytz
- **Propósito**: Manejo de zonas horarias
- **Uso**: Configurar la hora de Ciudad de México para la programación
- **Documentación**: [pytz.sourceforge.net](https://pytz.sourceforge.net)

### 🔐 python-dotenv
- **Propósito**: Cargar variables de entorno desde archivo .env
- **Uso**: Mantener credenciales y configuraciones sensibles seguras
- **Documentación**: [github.com/theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)

## 🔧 Instalación

### Instalación individual
```bash
pip install requests pandas openpyxl schedule pytz python-dotenv
```

### Instalación desde requirements.txt
```bash
pip install -r requirements.txt
```

### Instalación con versiones específicas (recomendado)
```bash
pip install requests==2.31.0 pandas==2.0.3 openpyxl==3.1.2 schedule==1.2.0 pytz==2023.3 python-dotenv==1.0.0
```

## 📋 Archivo requirements.txt

Crea un archivo llamado `requirements.txt` con el siguiente contenido:

```txt
requests==2.31.0
pandas==2.0.3
openpyxl==3.1.2
schedule==1.2.0
pytz==2023.3
python-dotenv==1.0.0
```

## 🐍 Compatibilidad de Python

- **Python mínimo**: 3.7+
- **Python recomendado**: 3.9+
- **Probado en**: 3.9, 3.10, 3.11

## 💻 Instalación por Sistema Operativo

### Windows
```cmd
pip install -r requirements.txt
```

### macOS/Linux
```bash
pip3 install -r requirements.txt
```

### Entorno virtual (recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🔍 Verificación de instalación

Para verificar que todas las librerías se instalaron correctamente:

```python
import requests
import pandas as pd
import openpyxl
import schedule
import pytz
from dotenv import load_dotenv

print("✅ Todas las librerías se importaron correctamente")
```

## 🚨 Troubleshooting

### Error común: "No module named 'xyz'"
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Error de permisos en Windows
```cmd
pip install --user -r requirements.txt
```

### Error de compilación en macOS/Linux
```bash
# Instalar dependencias del sistema
sudo apt-get install python3-dev  # Ubuntu/Debian
brew install python3  # macOS con Homebrew
```

## 📝 Notas adicionales

- Estas librerías son suficientes para la funcionalidad básica del proyecto
- Para el ejecutable con pyinstaller, no se requieren librerías adicionales
- Todas las librerías son compatibles entre sí en las versiones especificadas

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
