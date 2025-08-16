import random
import string
from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.codigo = self._generar_codigo()

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
    
    @abstractmethod
    def estado(self):
        pass

    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod     
    def devolver(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass