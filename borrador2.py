import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

# Constantes
TEMP_MIN = 18
TEMP_MAX = 30
RUTA_IMAGEN_DEFECTO = os.path.join("venv", "weed.jpg")
DATA_FILE = "data.json"

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
    elif sustrato ==  "húmedo":
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
        
        self.datos = self.cargar_datos()

    def configurar_interfaz(self):
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=0, column=0, columnspan=3, rowspan=10, padx=10, pady=10, sticky='nsew')

        # Pestaña de Datos
        frame_datos = ttk.Frame(notebook)
        notebook.add(frame_datos, text="Datos del Cultivo")

        tk.Label(frame_datos, text="Temperatura (°C):").grid(row=0, column=0, padx=10, pady=5)
        self.entry_temperatura = tk.Entry(frame_datos)
        self.entry_temperatura.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_datos, text="Crecimiento (rápido/lento):").grid(row=1, column=0, padx=10, pady=5)
        self.entry_crecimiento = tk.Entry(frame_datos)
        self.entry_crecimiento.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_datos, text="Floración (iniciando/avanzada):").grid(row=2, column=0, padx=10, pady=5)
        self.entry_floracion = tk.Entry(frame_datos)
        self.entry_floracion.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_datos, text="Sustrato (seco/húmedo):").grid(row=3, column=0, padx=10, pady=5)
        self.entry_sustrato = tk.Entry(frame_datos)
        self.entry_sustrato.grid(row=3, column=1, padx=10, pady=5)

        boton_obtener_ayuda = tk.Button(frame_datos, text="Obtener Ayuda", command=self.obtener_ayuda)
        boton_obtener_ayuda.grid(row=4, column=0, columnspan=2, pady=10)

        # Añadir Calendario
        self.calendario = Calendar(frame_datos, selectmode='day', year=2024, month=5, day=30)
        self.calendario.grid(row=5, column=0, columnspan=2, pady=10)

        # Botón para registrar datos
        boton_registrar_datos = tk.Button(frame_datos, text="Registrar Datos", command=self.registrar_datos)
        boton_registrar_datos.grid(row=6, column=0, columnspan=2, pady=10)

        # Botón para mostrar gráficos
        boton_mostrar_graficos = tk.Button(frame_datos, text="Mostrar Gráficos", command=self.mostrar_graficos)
        boton_mostrar_graficos.grid(row=7, column=0, columnspan=2, pady=10)

        # Pestaña de Guías y Tutoriales
        frame_guias = ttk.Frame(notebook)
        notebook.add(frame_guias, text="Guías y Tutoriales")

        text_guias = tk.Text(frame_guias, wrap=tk.WORD)
        text_guias.insert(tk.END, "Guías y Tutoriales:\n\n1. Guía de Cultivo: Instrucciones detalladas sobre cómo cultivar.\n2. Problemas Comunes: Soluciones para problemas comunes en el cultivo.\n3. Técnicas Avanzadas: Técnicas avanzadas de cultivo.\n")
        text_guias.config(state=tk.DISABLED)
        text_guias.grid(row=0, column=0, padx=10, pady=10)

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

    def cargar_datos(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        return []

    def guardar_datos(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.datos, file)

    def registrar_datos(self):
        try:
            fecha = self.calendario.get_date()
            temperatura = float(self.entry_temperatura.get())
            crecimiento = self.entry_crecimiento.get().lower()
            floracion = self.entry_floracion.get().lower()
            sustrato = self.entry_sustrato.get().lower()

            self.datos.append({
                "fecha": fecha,
                "temperatura": temperatura,
                "crecimiento": crecimiento,
                "floracion": floracion,
                "sustrato": sustrato
            })
            self.guardar_datos()
            messagebox.showinfo("Registro Exitoso", "Los datos han sido registrados correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def mostrar_graficos(self):
        if not self.datos:
            messagebox.showerror("Error", "No hay datos registrados para mostrar.")
            return

        fechas = [dato["fecha"] for dato in self.datos]
        temperaturas = [dato["temperatura"] for dato in self.datos]
        crecimiento = [dato["crecimiento"] for dato in self.datos]
        floracion = [dato["floracion"] for dato in self.datos]
        sustrato = [dato["sustrato"] for dato in self.datos]

        fig, axs = plt.subplots(4, 1, figsize=(10, 12))

        # Gráfico de Temperatura
        axs[0].plot(fechas, temperaturas, marker='o')
        axs[0].set(xlabel='Fecha', ylabel='Temperatura (°C)', title='Temperatura a lo largo del tiempo')
        axs[0].grid()

        # Gráfico de Crecimiento
        axs[1].plot(fechas, crecimiento, marker='o', linestyle='-', color='orange')
        axs[1].set(xlabel='Fecha', ylabel='Crecimiento', title='Crecimiento a lo largo del tiempo')
        axs[1].grid()

        # Gráfico de Floración
        axs[2].plot(fechas, floracion, marker='o', linestyle='-', color='green')
        axs[2].set(xlabel='Fecha', ylabel='Floración', title='Floración a lo largo del tiempo')
        axs[2].grid()

        # Gráfico de Sustrato
        axs[3].plot(fechas, sustrato, marker='o', linestyle='-', color='red')
        axs[3].set(xlabel='Fecha', ylabel='Sustrato', title='Sustrato a lo largo del tiempo')
        axs[3].grid()

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, column=0, columnspan=3, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CultivoApp(root)
    root.mainloop()
