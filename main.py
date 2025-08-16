from LibroDigital import LibroDigital
from LibroFisico import LibroFisico
from MaterialBiblioteca import MaterialBiblioteca

def menu():
    print("\n----------Biblioteca---------")
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Mostrar Información de Libros")
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
                    materialDigital = LibroDigital(titulo, autor, tamaño_archivo)
                    biblioteca.append(materialDigital)
                    print(f"Libro '{materialDigital.titulo}' agregado con código {materialDigital.codigo}")
                    break
                elif tipo == 'fisico':
                    no_ejemplares = int(input("Ingrese el número de ejemplares: "))
                    materialFisico = LibroFisico(titulo, autor, no_ejemplares)
                    biblioteca.append(materialFisico)
                    print(f"Libro '{materialFisico.titulo}' agregado con código {materialFisico.codigo}")
                    break
                else:
                    print("Tipo de Libro no válido. Intente nuevamente")

        elif opcion == '2':
            codigo = input("Ingrese el código del Libro a buscar: ")
            encontrado = False
            for material in biblioteca:
                if material.codigo == codigo:
                    material.mostrar_info()
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado.")
        
        elif opcion == '3':
            codigo = input("Ingrese el código del Libro a prestar: ")
            encontrado = False
            for material in biblioteca:
                if material.codigo == codigo:
                    material.prestar()
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado o no disponible para préstamo")

        elif opcion == '4':
            codigo = input("Ingrese el código del Libro a devolver: ")
            encontrado = False
            for material in biblioteca:
                if material.codigo == codigo:
                    material.devolver()
                    encontrado = True
                    break
            if not encontrado:
                print("Libro no encontrado o no está prestado")

        elif opcion == '5':
            if not biblioteca:
                print("No hay libros en la biblioteca")
            else:
                for material in biblioteca:
                    material.mostrar_info()

        elif opcion == '6':
            print("Saliendo del programa")
            break
                    
main()