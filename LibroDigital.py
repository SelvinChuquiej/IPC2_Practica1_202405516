from MaterialBiblioteca import MaterialBiblioteca

class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamaño_archivo):
        super().__init__(titulo, autor)
        self.tamaño_archivo = tamaño_archivo

    def prestar(self):
        if self.estado:
            print("Material no disponible")
        else:
            self.estado = True
            print(f"Material '{self.titulo}' prestado. Ejemplares restantes: {self.no_ejemplares}")
 
    def mostrar_info(self):
        estado = "Disponible" if not self.estado else "Prestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}, Exemplares disponibles: {self.no_ejemplares}")