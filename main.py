from LibroDigital import LibroDigital
from LibroFisico import LibroFisico

def menu():
    print("\n----------Biblioteca---------")
    print("1. Agregar Libro")
    print("6. Salir")
    print("-----------------------------")

def main():
    biblioteca = []

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del Libro: ")
            autor = input("Ingrese el autor del Libro: ")

            while True:
                tipo = input("Ingrese el tipo de Libro (digital/fisico): ").lower() 
                if tipo == 'digital':
                    tamaño_archivo = input("Ingrese el tamaño del archivo: ")
                    material = LibroDigital(titulo, autor, tamaño_archivo)
                    biblioteca.append(material)
                    print(f"Libro '{material.titulo}' agregado con código {material.codigo}.")
                    break
                elif tipo == 'fisico':
                    no_ejemplares = int(input("Ingrese el número de ejemplares: "))
                    material = LibroFisico(titulo, autor, no_ejemplares)
                    biblioteca.append(material)
                    print(f"Libro '{material.titulo}' agregado con código {material.codigo}.")
                    break
                else:
                    print("Tipo de Libro no válido. Intente nuevamente.")

        elif opcion == '6':
            print("Saliendo del programa.")
            break
                    
main()