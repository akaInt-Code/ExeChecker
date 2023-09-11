import os
import psutil
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

try:
    import psutil
except ImportError:
    os.system("pip install psutil")
    import psutil
    os.system("cls")

# Función para obtener la lista de ejecutables ejecutados en las últimas 12 horas
def obtener_ejecutables():
    tiempo_actual = datetime.datetime.now()
    limite_tiempo = tiempo_actual - datetime.timedelta(hours=12)
    ejecutables_ejecutados = []

    for proceso in psutil.process_iter(attrs=['name', 'exe', 'create_time']):
        try:
            proceso_info = proceso.info

            if datetime.datetime.fromtimestamp(proceso_info['create_time']) > limite_tiempo:
                ejecutable = proceso_info['name']
                fecha_ejecucion = datetime.datetime.fromtimestamp(proceso_info['create_time'])
                ubicacion_archivo = proceso_info['exe']

                ejecutables_ejecutados.append((ejecutable, fecha_ejecucion, ubicacion_archivo))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return ejecutables_ejecutados

# Función para actualizar los resultados
def actualizar_resultados():
    ejecutables = obtener_ejecutables()
    resultados_text.config(state=tk.NORMAL)
    resultados_text.delete('1.0', tk.END)
    for ejecutable, fecha_ejecucion, ubicacion_archivo in ejecutables:
        resultados_text.insert(tk.END, f"Ejecutable: {ejecutable}\n")
        resultados_text.insert(tk.END, f"Fecha de ejecución: {fecha_ejecucion}\n")
        resultados_text.insert(tk.END, f"Ubicación del archivo: {ubicacion_archivo}\n")
        resultados_text.insert(tk.END, "=" * 50 + "\n")
    resultados_text.config(state=tk.DISABLED)

# Función para guardar los resultados en un archivo .txt
def guardar_resultados():
    ejecutables = obtener_ejecutables()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for ejecutable, fecha_ejecucion, ubicacion_archivo in ejecutables:
                file.write(f"Ejecutable: {ejecutable}\n")
                file.write(f"Fecha de ejecución: {fecha_ejecucion}\n")
                file.write(f"Ubicación del archivo: {ubicacion_archivo}\n")
                file.write("=" * 50 + "\n")

# Crear una ventana de GUI
ventana = tk.Tk()
ventana.title("ExeChecker | By JustCode")
ventana.geometry("600x400")

# Configurar el icono de la ventana
ventana.iconbitmap("icono.ico") 

# Crear un marco principal para el diseño
frame_principal = ttk.Frame(ventana)
frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Título
titulo_label = ttk.Label(frame_principal, text="Ejecutables en las últimas 12 horas", font=("Arial", 16))
titulo_label.pack(pady=10)

# Botón para actualizar los resultados
actualizar_button = ttk.Button(frame_principal, text="Actualizar", command=actualizar_resultados)
actualizar_button.pack(pady=5)

# Botón para guardar los resultados
guardar_button = ttk.Button(frame_principal, text="Guardar en archivo .txt", command=guardar_resultados)
guardar_button.pack(pady=5)

# Área de texto con barra de desplazamiento
frame_texto = ttk.Frame(frame_principal)
frame_texto.pack(fill=tk.BOTH, expand=True)

resultados_text = scrolledtext.ScrolledText(frame_texto, wrap=tk.WORD, state=tk.DISABLED)
resultados_text.pack(fill=tk.BOTH, expand=True)

# Botón para guardar los resultados en un archivo .txt
guardar_button = ttk.Button(frame_principal, text="Guardar en archivo .txt", command=guardar_resultados)
guardar_button.pack(pady=5)

# Función para actualizar los resultados al inicio
def iniciar():
    actualizar_resultados()

# Ejecutar la función de inicio
iniciar()

# Ejecutar la GUI
ventana.mainloop()
