class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, velocidad {self.velocidad} Km/h, cilindrada {self.cilindrada} cc"


cantidad_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))

automoviles = []

for i in range(cantidad_vehiculos):
    print(f"\nDatos del automóvil {i + 1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    nro_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))

    automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
    automoviles.append(automovil)

print("\nImprimiendo por pantalla los Vehículos:")
for i, automovil in enumerate(automoviles, start=1):
    print(f"Datos del automóvil {i}: {automovil}")

    
from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

print("Motocicleta es instancia con relación a Vehiculo: ", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil: ", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular: ", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga: ", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta: ", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta: ", isinstance(motocicleta, Motocicleta))
        
from vehiculo import Particular, Carga, Bicicleta, Motocicleta
from gestion_csv import guardar_datos_csv, leer_datos_csv

if __name__ == "__main__":
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    guardar_datos_csv([particular, carga, bicicleta, motocicleta])

    leer_datos_csv()
    
    
    class Vehiculo:
        def __init__(self, marca, modelo, nro_ruedas):
            self.marca = marca
            self.modelo = modelo
            self.nro_ruedas = nro_ruedas

        def __str__(self):
            return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

