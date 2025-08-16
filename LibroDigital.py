from MaterialBiblioteca import MaterialBiblioteca

class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamaño_archivo):
        super().__init__(titulo, autor)
        self.tamaño_archivo = tamaño_archivo
        self._prestado = False

    @property
    def tamaño_archivo(self):
        return self._tamaño_archivo 
    
    @tamaño_archivo.setter
    def tamaño_archivo(self, value):
        value = float(value)
        if value > 0:
            self._tamaño_archivo = value
        else:
            raise ValueError("El tamaño del archivo debe ser un número positivo")
    
    def estado(self):
        return not self._prestado #True

    def prestar(self):
        if not self.estado:
            print(f"Libro '{self.titulo}' no disponible para prestamo")
        else:
            self.estado = True
            print(f"Libro '{self.titulo}' prestado")

    def devolver(self):
        if not self.estado:
            print(f"Libro'{self.titulo}' no está prestado")
        else:
            self.estado = False
            print(f"Libro'{self.titulo}' devuelto")
 
    def mostrar_info(self):
        estado = "Disponible" if not self.estado else "Prestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}, Tamaño del archivo: {self.tamaño_archivo} MB")