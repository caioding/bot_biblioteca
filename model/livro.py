from .autor import Autor

class Livro:
    def __init__(self, titulo: str, autor: Autor, codigo: str):
        self.__titulo = titulo
        self.autor = Autor(autor.nome)
        self.__codigo = codigo
        self.__emprestimo_disponivel = True
        autor.adicionar_livro(self)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def condigo(self, novo_codigo):
        self.__codigo = novo_codigo
    
    @property
    def emprestimo_disponivel(self):
        return self.__emprestimo_disponivel

    @emprestimo_disponivel.setter
    def emprestimo_disponivel(self, novo_emprestimo_disponivel):
        self.__emprestimo_disponivel = novo_emprestimo_disponivel

    def emprestar(self):
        self.__emprestimo_disponivel = False
    
    def devolver(self):
        self.__emprestimo_disponivel = True
