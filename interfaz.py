import tkinter as tk
from tkinter import ttk
import threading
import requests
import time
import subprocess
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Logica del "ataque" controlado ---
def lanzar_ataque(n, output_box, update_cpu_graph):
    url = "http://127.0.0.1:8000/lento"#puede ir cualquier url, 
    #pero para este ejemplo usamos la ruta lenta del servidor Flask
    threads = []
    resultados = []

    stop_cpu_monitor.clear()  # Señal para iniciar el monitoreo de CPU

    def flood():
        try:
            r = requests.get(url, timeout=5)
            resultados.append(f"✔ {r.status_code}")
        except Exception as e:
            resultados.append(f"✖ {str(e)}")

    inicio = time.time()
    for _ in range(n):
        t = threading.Thread(target=flood)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    fin = time.time()

    stop_cpu_monitor.set()  # Señal para detener el monitoreo de CPU

    output_box.insert(tk.END, f"\n🔵 Ataque simulado con {n} hilos\n")
    for r in resultados:
        output_box.insert(tk.END, f"{r}\n")
    output_box.insert(tk.END, f"⏱ Tiempo total: {fin - inicio:.2f} s\n\n")
    output_box.see(tk.END)

# --- Monitor de CPU ---
stop_cpu_monitor = threading.Event()

def monitor_cpu(fig, ax, canvas):
    cpu_usage = []
    times = []
    start_time = time.time()

    while not stop_cpu_monitor.is_set():
        usage = psutil.cpu_percent(interval=0.5)
        elapsed = time.time() - start_time
        cpu_usage.append(usage)
        times.append(elapsed)

        ax.clear()
        ax.plot(times, cpu_usage, color="blue")
        ax.set_ylim(0, 100)
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("CPU %")
        ax.set_title("Uso de CPU durante la simulacion")
        ax.grid(True)
        canvas.draw()

    # Una ultima actualizacion para que quede el grafico final
    ax.clear()
    ax.plot(times, cpu_usage, color="blue")
    ax.set_ylim(0, 100)
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("CPU %")
    ax.set_title("Uso de CPU durante la simulacion")
    ax.grid(True)
    canvas.draw()

# --- Logica para iniciar el servidor Flask ---
def iniciar_servidor(output_box):
    try:
        subprocess.Popen(["python", "server.py"])
        output_box.insert(tk.END, "✅ Servidor iniciado en http://127.0.0.1:8000\n")
        output_box.see(tk.END)
    except Exception as e:
        output_box.insert(tk.END, f"⚠️ Error al iniciar el servidor: {e}\n")
        output_box.see(tk.END)

# --- Interfaz grafica ---
def main():
    root = tk.Tk()
    root.title("Simulador DDoS Local - Educativo")
    root.geometry("700x600")
    root.configure(bg="#D0E4F5")  # Azul claro

    titulo = tk.Label(root, text="Simulador DDoS (solo local)", bg="#D0E4F5", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    btn_servidor = tk.Button(root, text="Iniciar Servidor Flask", command=lambda: iniciar_servidor(output_box), bg="#66A3D2", fg="white")
    btn_servidor.pack(pady=5)

    frame = tk.Frame(root, bg="#D0E4F5")
    frame.pack(pady=10)

    tk.Label(frame, text="Cantidad de solicitudes:", bg="#D0E4F5").pack(side="left", padx=5)
    cantidad = tk.IntVar(value=50)
    spinbox = tk.Spinbox(frame, from_=10, to=500, increment=10, textvariable=cantidad, width=6)
    spinbox.pack(side="left")

    btn_ataque = tk.Button(root, text="Lanzar Simulación", bg="#007ACC", fg="white")
    btn_ataque.pack(pady=5)

    output_box = tk.Text(root, height=12, width=80)
    output_box.pack(padx=10, pady=10)

    # --- Configurar gráfico matplotlib ---
    fig, ax = plt.subplots(figsize=(7, 3))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # funcion que arranca el ataque y el monitoreo
    def ataque_y_monitor():
        stop_cpu_monitor.clear()
        monitor_thread = threading.Thread(target=monitor_cpu, args=(fig, ax, canvas))
        monitor_thread.start()

        lanzar_ataque(cantidad.get(), output_box, None)

        stop_cpu_monitor.set()
        monitor_thread.join()

    btn_ataque.config(command=lambda: threading.Thread(target=ataque_y_monitor).start())

    root.mainloop()

if __name__ == "__main__":
    main()
