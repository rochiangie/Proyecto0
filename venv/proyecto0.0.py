import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Función para cargar la imagen como fondo
def cargar_fondo(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((ventana.winfo_width(), ventana.winfo_height()))
        imagen_fondo = ImageTk.PhotoImage(imagen)

        label_fondo.config(image=imagen_fondo)
        label_fondo.image = imagen_fondo  # Para evitar que la imagen sea recolectada por el garbage collector
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Función para establecer la imagen de fondo específica
def seleccionar_imagen():
    ruta_imagen = r"C:\Users\rocio\Documents\GitHub\Proyecto0\Proyecto0\venv\weed.jpg"
    if ruta_imagen:
        cargar_fondo(ruta_imagen)


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Asistente de Cultivo de Marihuana")

# Crear un Label que actuará como fondo
label_fondo = tk.Label(ventana)
label_fondo.place(relwidth=1, relheight=1)

# Cargar la imagen de fondo al inicio
ventana.after(100, seleccionar_imagen)

# Resto del código de la aplicación (labels, entries y botones)
tk.Label(ventana, text="Temperatura (°C):").grid(row=0, column=0, padx=10, pady=5)
entry_temperatura = tk.Entry(ventana)
entry_temperatura.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Crecimiento (rápido/lento):").grid(row=1, column=0, padx=10, pady=5)
entry_crecimiento = tk.Entry(ventana)
entry_crecimiento.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Floración (iniciando/avanzada):").grid(row=2, column=0, padx=10, pady=5)
entry_floracion = tk.Entry(ventana)
entry_floracion.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Sustrato (seco/húmedo):").grid(row=3, column=0, padx=10, pady=5)
entry_sustrato = tk.Entry(ventana)
entry_sustrato.grid(row=3, column=1, padx=10, pady=5)

btn_obtener_ayuda = tk.Button(ventana, text="Obtener Ayuda", command=lambda: messagebox.showinfo("Recomendaciones", "Aquí van las recomendaciones"))
btn_obtener_ayuda.grid(row=4, column=0, columnspan=2, pady=10)

# Ajustar el tamaño de la ventana
ventana.geometry("800x600")

# Iniciar el loop de la ventana
ventana.mainloop()
