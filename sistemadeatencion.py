class Paciente:
    def __init__(self, nombre, edad, dpi, tipo_sangre, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.dpi = dpi
        self.tipo_sangre = tipo_sangre
        self.prioridad = prioridad

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, edad={self.edad}, dpi={self.dpi}, prioridad={self.prioridad})"


class SistemaAtencion:
    def __init__(self):
        self.cola_pacientes = []

    def agregar_paciente(self, paciente):
        self.cola_pacientes.append(paciente)
        self.cola_pacientes.sort(key=lambda x: x.prioridad)

    def atender_paciente(self):
        if self.cola_pacientes:
            return self.cola_pacientes.pop(0)
        else:
            return None

    def imprimir_cola(self):
        for paciente in self.cola_pacientes:
            print(paciente)


# Funcion principal para la interacción
def main():
    sistema = SistemaAtencion()

    while True:
        print("\nSistema de Atención a Pacientes")
        print("1. Agregar Paciente")
        print("2. Atender Paciente")
        print("3. Imprimir Cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            dpi = input("DPI: ")
            tipo_sangre = input("Tipo de Sangre: ")
            prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
            paciente = Paciente(nombre, edad, dpi, tipo_sangre, prioridad)
            sistema.agregar_paciente(paciente)
            print(f"Paciente {nombre} agregado a la cola.")

        elif opcion == '2':
            paciente_atendido = sistema.atender_paciente()
            if paciente_atendido:
                print(f"Atendiendo a: {paciente_atendido}")
            else:
                print("No hay pacientes en la cola.")

        elif opcion == '3':
            sistema.imprimir_cola()

        elif opcion == '4':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()