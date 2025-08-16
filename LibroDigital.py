from MaterialBiblioteca import MaterialBiblioteca

class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamaño_archivo):
        super().__init__(titulo, autor)
        self.tamaño_archivo = tamaño_archivo

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
    
    def prestar(self):
        if self.estado:
            print("Libro no disponible")
        else:
            self.estado = True
            print(f"Libro '{self.titulo}' prestado")
 
    def mostrar_info(self):
        estado = "Disponible" if not self.estado else "Prestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}, Tamaño del archivo: {self.tamaño_archivo}")