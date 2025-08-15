import random
import string

class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.codigo = self._generar_codigo()
        self.estado = False

    def _generar_codigo(self):
        codigo = string.ascii_letters + string.digits
        return ''.join(random.choice(codigo) for _ in range(8))

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def codigo(self):
        return self._codigo 
 
    @property
    def estado(self):
        return self._estado
 
    
    def prestar(self):        
        if self.estado:
            print("Material no disponible")
        else:
            self.estado = True
            print(f"Material '{self._titulo}' prestado")
            
    def devolver(self):
        if not self.estado:
            print("Material no esta prestado")
        else:
            self.estado = False
            print("Material '{self._titulo}' devuelto")

    def mostrar_info(self):
        estado = "Disponible" if not self.estado else "Prestado"
        print(f"Título: {self._titulo}, Autor: {self._autor}, Código: {self._codigo}, Estado: {estado}")