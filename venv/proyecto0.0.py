import tkinter as tk
from tkinter import messagebox

# Funciones para proporcionar recomendaciones
def obtener_recomendacion(temperatura, crecimiento, floracion, sustrato):
    # Aquí puedes agregar la lógica para generar recomendaciones basadas en los inputs
    recomendaciones = []
    
    # Ejemplo de recomendaciones simples
    if temperatura < 18:
        recomendaciones.append("La temperatura es muy baja. Considera calentar el ambiente.")
    elif temperatura > 30:
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

# Función que se ejecuta al hacer clic en el botón
def obtener_ayuda():
    try:
        temperatura = float(entry_temperatura.get())
        crecimiento = entry_crecimiento.get().lower()
        floracion = entry_floracion.get().lower()
        sustrato = entry_sustrato.get().lower()

        recomendacion = obtener_recomendacion(temperatura, crecimiento, floracion, sustrato)
        messagebox.showinfo("Recomendaciones", recomendacion)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Asistente de Cultivo de Marihuana")

# Labels y entradas de texto
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

# Botón para obtener recomendaciones
btn_obtener_ayuda = tk.Button(ventana, text="Obtener Ayuda", command=obtener_ayuda)
btn_obtener_ayuda.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
