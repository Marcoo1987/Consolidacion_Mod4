from vehiculo import Automovil #revisar bien esto
import csv

def guardar_datos_csv(objetos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for obj in objetos:
                archivo_csv.writerow([obj.__class__.__name__, obj.__dict__])
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")


def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for row in archivo_csv:
                print(row)
    except Exception as e:
        print(f"Error al leer desde CSV: {e}")
