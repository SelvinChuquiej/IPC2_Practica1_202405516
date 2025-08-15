class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, estado):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.estado = estado

    def devolver(self):
        self.estado = "disponível"

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {self.estado}"