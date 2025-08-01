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
