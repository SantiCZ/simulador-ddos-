# simulador-ddos-
un programa que simula un ddos al servidor hecho con flask 
# 🛡️ Simulador de DDoS Local (Educativo)

Este proyecto permite simular un **ataque DDoS controlado** en un entorno completamente local con fines **educativos y de monitoreo de recursos**. La aplicación cuenta con una interfaz gráfica que lanza múltiples solicitudes simultáneas a un servidor Flask local, mientras grafica el uso de CPU en tiempo real.

---

## 📁 Archivos del Proyecto

### `interfaz.py`

Contiene la **interfaz gráfica en Tkinter**, desde la cual el usuario puede:

- Iniciar un servidor Flask local.
- Seleccionar el número de solicitudes a enviar.
- Lanzar una simulación de ataque DDoS (requests paralelos).
- Ver los resultados en un cuadro de texto.
- Observar en tiempo real un gráfico del uso de CPU durante el "ataque".

### `server.py`

Servidor web básico hecho con Flask que expone dos rutas:

- `/`: Responde rápidamente con "Servidor activo".
- `/lento`: Simula una ruta lenta con `sleep(2)`, para imitar un endpoint vulnerable a saturación.

---

## 🚀 ¿Cómo se usa?

1. Asegúrate de tener **Python 3** instalado.
2. Instala los módulos necesarios si no los tienes:
   ```
   pip install flask psutil matplotlib requests
   ```
3. Ejecuta el archivo principal:
   ```
   python interfaz.py
   ```
4. Desde la interfaz:
   - Haz clic en **“Iniciar Servidor Flask”**.
   - Ajusta la cantidad de solicitudes simultáneas (hilos).
   - Presiona **“Lanzar Simulación”** para iniciar el "ataque" a la ruta `/lento`.

---

## 📊 ¿Qué hace el sistema?

- Lanza múltiples hilos (`Thread`) que hacen `GET` a `http://127.0.0.1:8000/lento`.
- Mide el tiempo total que tomó completar todas las solicitudes.
- Muestra el estado HTTP de cada respuesta (`200 OK` o errores).
- Dibuja un gráfico de **uso de CPU** a lo largo del tiempo usando `matplotlib`.

---

## ⚠️ Advertencia

Este proyecto está **diseñado únicamente para fines educativos y de prueba local**. No debe utilizarse para atacar servidores reales ni redes externas. Hacerlo puede ser ilegal y está fuera del alcance y propósito de este software.

---

## 📌 Requisitos

- Python 3.7 o superior
- Módulos:
  - `flask`
  - `requests`
  - `tkinter` (incluido por defecto en la mayoría de las instalaciones de Python)
  - `matplotlib`
  - `psutil`

## ⚖️ ❗ Consideraciones Legales y Éticas

- **Lanzar múltiples solicitudes simultáneas a un servidor sin permiso** puede ser considerado un **ataque DDoS real**, lo cual es **ilegal en casi todos los países**, incluso si el daño es mínimo o no intencional.
- Aunque tú seas el dueño del servidor, si está en la nube (por ejemplo, AWS, Azure, etc.), podría violar los **términos de servicio** y provocar sanciones, bloqueos o costos inesperados.
- Hacer esto sin autorización puede **comprometer tu conexión**, **afectar a otros usuarios** y **generar repercusiones legales** graves.

---

## 🧪 ¿En qué casos sería aceptable?

- Si el servidor **es completamente tuyo**, está **en red local o virtual**, y su objetivo es **pruebas de estrés controladas**.
- Usando herramientas de protección para asegurar que el "ataque" no afecte a terceros (limitando ancho de banda, número de hilos, duración, etc.).
- Siempre dejando en claro que se trata de una **prueba de carga con propósito educativo, de benchmarking o de hardening**.

---

## ⚙️ ¿Cómo cambiarlo para usar un servidor real?

Si estás autorizado, puedes cambiar esta linea en `interfaz.py`:
```
url = "http://127.0.0.1:8000/lento"
```
por una URL real:
```
url = "https://mi-servidor-real.com/api/prueba"
```
Y asegurar que el servidor este diseñado para manejar esta carga. Pero **nunca lo hagas sin autorizacion clara y escrita, creo que no es necesario recalcar que hacer lo contrario seria ilegal**.
