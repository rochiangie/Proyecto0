import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def cargar_fondo(ruta_imagen):
    """Carga una imagen y la establece como fondo de la ventana."""
    try:
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((ventana.winfo_width(), ventana.winfo_height()))
        imagen_fondo = ImageTk.PhotoImage(imagen)

        label_fondo.config(image=imagen_fondo)
        label_fondo.image = imagen_fondo  # Evitar recolección de basura
    except FileNotFoundError:
        messagebox.showerror("Error", "La imagen no se encontró en la ruta especificada.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

def seleccionar_imagen():
    """Selecciona una imagen y la carga como fondo de la ventana."""
    # Ruta relativa a la imagen
    ruta_imagen = os.path.join("proyecto0", "weed.jpg")
    if os.path.exists(ruta_imagen):
        cargar_fondo(ruta_imagen)
    else:
        messagebox.showerror("Error", "La imagen no se encontró en la ruta especificada.")

def configurar_interfaz():
    """Configura la interfaz de usuario."""
    label_fondo.place(relwidth=1, relheight=1)

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

    boton_obtener_ayuda = tk.Button(ventana, text="Obtener Ayuda", command=mostrar_recomendaciones)
    boton_obtener_ayuda.grid(row=4, column=0, columnspan=2, pady=10)

def mostrar_recomendaciones():
    """Muestra las recomendaciones al usuario."""
    messagebox.showinfo("Recomendaciones", "Aquí van las recomendaciones.")

ventana = tk.Tk()
ventana.title("Asistente de Cultivo de Marihuana")

label_fondo = tk.Label(ventana)

configurar_interfaz()
ventana.after(100, seleccionar_imagen)

ventana.geometry("800x600")
ventana.mainloop()
