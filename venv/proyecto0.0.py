from datetime import date

class RegistroDiario:
    def __init__(self, fecha, temperatura, humedad, caracteristicas):
        self.fecha = fecha
        self.temperatura = temperatura
        self.humedad = humedad
        self.caracteristicas = caracteristicas

class Planta:
    def __init__(self, nombre, caracteristicas, fecha_plantado):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        self.fecha_plantado = fecha_plantado
        self.historial = []

    def agregar_registro(self, registro):
        self.historial.append(registro)
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Características: {self.caracteristicas}")
        print(f"Fecha de Plantado: {self.fecha_plantado}")
        print("Historial de Seguimiento:")
        for registro in self.historial:
            print(f"  Fecha: {registro.fecha}")
            print(f"  Temperatura: {registro.temperatura}")
            print(f"  Humedad: {registro.humedad}")
            print(f"  Características: {registro.caracteristicas}")
            print("-" * 20)

# Ejemplo de uso
# Crear una planta
planta = Planta("Rosa", "Roja, Espinosa", date(2024, 5, 1))

# Agregar registros diarios
registro1 = RegistroDiario(date(2024, 5, 10), 25, 60, "Follaje verde y saludable")
registro2 = RegistroDiario(date(2024, 5, 15), 26, 58, "Floración comenzando")

planta.agregar_registro(registro1)
planta.agregar_registro(registro2)

# Mostrar información de la planta
planta.mostrar_informacion()

class GestorPlantas:
    def __init__(self):
        self.plantas = []

    def agregar_planta(self, planta):
        self.plantas.append(planta)

    def mostrar_plantas(self):
        for planta in self.plantas:
            planta.mostrar_informacion()
            print("=" * 30)

# Ejemplo de uso
# Crear el gestor de plantas
gestor = GestorPlantas()

# Crear y agregar plantas al gestor
planta1 = Planta("Rosa", "Roja, Espinosa", date(2024, 5, 1))
planta2 = Planta("Tulipán", "Amarillo, Delicado", date(2024, 5, 2))

gestor.agregar_planta(planta1)
gestor.agregar_planta(planta2)

# Agregar registros a las plantas
registro1_planta1 = RegistroDiario(date(2024, 5, 10), 25, 60, "Follaje verde y saludable")
registro2_planta1 = RegistroDiario(date(2024, 5, 15), 26, 58, "Floración comenzando")
planta1.agregar_registro(registro1_planta1)
planta1.agregar_registro(registro2_planta1)

registro1_planta2 = RegistroDiario(date(2024, 5, 10), 20, 65, "Crecimiento saludable")
registro2_planta2 = RegistroDiario(date(2024, 5, 15), 21, 63, "Primeros brotes")
planta2.agregar_registro(registro1_planta2)
planta2.agregar_registro(registro2_planta2)

# Mostrar información de todas las plantas
gestor.mostrar_plantas()
