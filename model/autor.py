class Autor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__livros = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def livros(self):
        return self.__livros

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def mostrar_livros(self):
        for livro in self.__livros:
            print(livro.titulo)

