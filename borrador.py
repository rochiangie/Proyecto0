import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Constantes
TEMP_MIN = 18
TEMP_MAX = 30
RUTA_IMAGEN_DEFECTO = os.path.join("venv", "weed.jpg")

# Funciones para proporcionar recomendaciones
def obtener_recomendacion(temperatura, crecimiento, floracion, sustrato):
    recomendaciones = []

    if temperatura < TEMP_MIN:
        recomendaciones.append("La temperatura es muy baja. Considera calentar el ambiente.")
    elif temperatura > TEMP_MAX:
        recomendaciones.append("La temperatura es muy alta. Considera enfriar el ambiente.")
    else:
        recomendaciones.append("La temperatura es adecuada.")

    if crecimiento == "lento":
        recomendaciones.append("El crecimiento es lento. Revisa los nutrientes y la luz.")
    elif crecimiento == "rápido":
        recomendaciones.append("El crecimiento es bueno. Continúa con los cuidados actuales.")

    if floracion == "iniciando":
        recomendaciones.append("La floración está iniciando. Ajusta el fotoperiodo a 12 horas de luz y 12 horas de oscuridad.")
    elif floracion == "avanzada":
        recomendaciones.append("La floración está avanzada. Mantén los cuidados actuales y prepara para la cosecha.")

    if sustrato == "seco":
        recomendaciones.append("El sustrato está seco. Necesita más riego.")
    elif sustrato == "húmedo":
        recomendaciones.append("El sustrato está húmedo. Riega con menos frecuencia.")

    return "\n".join(recomendaciones)

class CultivoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente de Cultivo de Marihuana")
        self.root.geometry("800x600")

        self.label_fondo = tk.Label(root)
        self.label_fondo.place(relwidth=1, relheight=1)

        self.configurar_interfaz()
        self.root.bind('<Configure>', self.redimensionar_fondo)
        self.cargar_fondo(RUTA_IMAGEN_DEFECTO)
        
    def configurar_interfaz(self):
        tk.Label(self.root, text="Temperatura (°C):").grid(row=0, column=0, padx=10, pady=5)
        self.entry_temperatura = tk.Entry(self.root)
        self.entry_temperatura.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Crecimiento (rápido/lento):").grid(row=1, column=0, padx=10, pady=5)
        self.entry_crecimiento = tk.Entry(self.root)
        self.entry_crecimiento.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Floración (iniciando/avanzada):").grid(row=2, column=0, padx=10, pady=5)
        self.entry_floracion = tk.Entry(self.root)
        self.entry_floracion.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Sustrato (seco/húmedo):").grid(row=3, column=0, padx=10, pady=5)
        self.entry_sustrato = tk.Entry(self.root)
        self.entry_sustrato.grid(row=3, column=1, padx=10, pady=5)

        boton_obtener_ayuda = tk.Button(self.root, text="Obtener Ayuda", command=self.obtener_ayuda)
        boton_obtener_ayuda.grid(row=4, column=0, columnspan=2, pady=10)

    def obtener_ayuda(self):
        try:
            temperatura = float(self.entry_temperatura.get())
            crecimiento = self.entry_crecimiento.get().lower()
            floracion = self.entry_floracion.get().lower()
            sustrato = self.entry_sustrato.get().lower()

            recomendacion = obtener_recomendacion(temperatura, crecimiento, floracion, sustrato)
            messagebox.showinfo("Recomendaciones", recomendacion)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def cargar_fondo(self, ruta_imagen):
        try:
            self.imagen = Image.open(ruta_imagen)
            self.redimensionar_fondo()
        except FileNotFoundError:
            messagebox.showerror("Error", "La imagen no se encontró en la ruta especificada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def redimensionar_fondo(self, event=None):
        if hasattr(self, 'imagen'):
            imagen_redimensionada = self.imagen.resize((self.root.winfo_width(), self.root.winfo_height()))
            self.imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)
            self.label_fondo.config(image=self.imagen_fondo)
            self.label_fondo.image = self.imagen_fondo  # Evitar recolección de basura

if __name__ == "__main__":
    root = tk.Tk()
    app = CultivoApp(root)
    root.mainloop()
