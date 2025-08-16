from MaterialBiblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, no_ejemplares):
        super().__init__(titulo, autor)
        self.no_ejemplares = no_ejemplares

    @property
    def no_ejemplares(self):
        return self._no_ejemplares
    
    @no_ejemplares.setter
    def no_ejemplares(self, value): 
        value = int(value)
        if value > 0:
            self._no_ejemplares = value
        else:
            raise ValueError("El número de ejemplares debe ser un entero positivo.")

    def prestar(self):
        if self.estado:
            print("Libro no disponible")
        else:
            self.estado = True
            print(f"Libro '{self.titulo}' prestado. Ejemplares restantes: {self.no_ejemplares}")
 
    def mostrar_info(self):
        estado = "Disponible" if not self.estado else "Prestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}, Exemplares disponibles: {self.no_ejemplares}")