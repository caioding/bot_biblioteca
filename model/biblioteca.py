from .livro import Livro
from .autor import Autor

class Biblioteca:
    total_livros = 0

    def __init__(self, nome_biblioteca: str):
        self.nome_biblioteca = nome_biblioteca
        self.__livros_biblioteca = []
        self.__emprestimos = {}

    @property
    def livros_biblioteca(self):
        return self.__livros_biblioteca
    
    @livros_biblioteca.setter
    def livros_biblioteca(self, novos_livros):
        self.__livros_biblioteca = novos_livros
    
    @property
    def emprestimos(self):
        return self.__emprestimos
    
    @emprestimos.setter
    def emprestimos(self, novos_emprestimos):
        self.__emprestimos = novos_emprestimos

    def adicionar_livro(self, livro: Livro):
        self.__livros_biblioteca.append(livro)
        Biblioteca.total_livros += 1

    def registrar_emprestimo(self, codigo_livro: str, cliente: str):
        for livro in self.__livros_biblioteca:
            if livro.codigo == codigo_livro and livro.emprestimo_disponivel:
                livro.emprestar()
                self.__emprestimos[codigo_livro] = cliente
                return f"Livro {livro.titulo} emprestado para {cliente}."
        return "Livro não disponível para empréstimo."
    
    def registrar_devolucao(self, codigo_livro: str):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros_biblioteca:
                if livro.codigo == codigo_livro:
                    livro.devolver()
                    del self.__emprestimos[codigo_livro]
                    return f"Livro {livro.titulo} devolvido."
        return "Livro não encontrado nos empréstimos."

    def mostrar_livros_disponiveis(self):
        for livro in self.__livros_biblioteca:
            if livro.emprestimo_disponivel:
                print(f'Título: {livro.titulo}, Autor: {livro.autor.nome}')

    @classmethod
    def mostrar_total_livros(cls, biblioteca):
        total_livros = cls.total_livros
        total_emprestados = len(biblioteca.emprestimos)
        total_disponiveis = total_livros - total_emprestados
        print(f"Total de livros na biblioteca: {total_livros}")
        print(f"Total de livros disponíveis: {total_disponiveis}")