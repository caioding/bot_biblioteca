from model.autor import Autor
from model.livro import Livro
from model.biblioteca import Biblioteca

def main():
    # Criando instâncias de Autor
    autor1 = Autor("J.K. Rowling")
    autor2 = Autor("George R.R. Martin")

    # Criando instâncias de Livro
    livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, "HP1")
    livro2 = Livro("Harry Potter e a Câmara Secreta", autor1, "HP2")
    livro3 = Livro("A Guerra dos Tronos", autor2, "GOT1")
    livro4 = Livro("A Fúria dos Reis", autor2, "GOT2")

    # Criando instância de Biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Adicionando livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)

    # Mostrando livros disponíveis
    print("Livros disponíveis na biblioteca:")
    biblioteca.mostrar_livros_disponiveis()

    # Registrando empréstimo
    print(biblioteca.registrar_emprestimo("HP1", "Maria"))
    print(biblioteca.registrar_emprestimo("GOT1", "João"))

    # Mostrando livros disponíveis após empréstimo
    print("Livros disponíveis na biblioteca após empréstimos:")
    biblioteca.mostrar_livros_disponiveis()

    # Registrando devolução
    print(biblioteca.registrar_devolucao("HP1"))

    # Mostrando livros disponíveis após devolução
    print("Livros disponíveis na biblioteca após devolução:")
    biblioteca.mostrar_livros_disponiveis()

    # Mostrando total de livros na biblioteca
    Biblioteca.mostrar_total_livros(biblioteca)  # Usando o método de classe

if __name__ == '__main__':
    main()