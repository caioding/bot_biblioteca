# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Add
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin

# Add for path OS
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# Import modelels
from models import Livro, Autor, Emprestimo, Biblioteca

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Functions for bot input forms
def preencher_formulario_autor(bot, nome):

    bot.browse("http://127.0.0.1:8000")
    bot.wait(3000)
    bot.find_element("/html/body/form[1]/input", By.XPATH).send_keys(nome)
    autor_button = bot.find_element("/html/body/form[1]/button", By.XPATH)
    if autor_button:
        autor_button.click()
        print(f"Formulário de autor preenchido com: Nome={nome}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source) 

def preencher_formulario_livro(bot, titulo, codigo):

    bot.browse("http://127.0.0.1:8000") 
    bot.wait(3000)
    bot.find_element("/html/body/form[2]/input[1]", By.XPATH).send_keys(titulo)
    bot.find_element("/html/body/form[2]/input[2]", By.XPATH).send_keys(codigo)
    bot.find_element("/html/body/form[2]/select", By.XPATH).click()
    # bot.find_element("/html/body/form[2]/select/option[3]", By.XPATH).click()
    livro_button = bot.find_element("/html/body/form[2]/button", By.XPATH)
    if livro_button:
        livro_button.click()
        print(f"Formulário de livro preenchido com: Título={titulo}, Código={codigo}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source)

def preencher_formulario_biblioteca(bot, nome):

    bot.browse("http://127.0.0.1:8000")
    bot.wait(3000)
    bot.find_element("/html/body/form[3]/input", By.XPATH).send_keys(nome)
    biblioteca_button = bot.find_element("/html/body/form[3]/button", By.XPATH)
    if biblioteca_button:
        biblioteca_button.click()
        print(f"Formulário de biblioteca preenchido com: Nome={nome}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source)

def preencher_formulario_emprestimo(bot, titulo, cliente, data_emprestimo):

    bot.browse("http://127.0.0.1:8000")
    bot.wait(3000)
    bot.find_element("/html/body/form[4]/select", By.XPATH).click()
    bot.find_element("/html/body/form[4]/select", By.XPATH).send_keys(titulo)
    bot.find_element("/html/body/form[4]/input[1]", By.XPATH).send_keys(cliente)
    bot.find_element("/html/body/form[4]/input[2]", By.XPATH).send_keys(data_emprestimo)
    emprestimo_button = bot.find_element("/html/body/form[4]/button", By.XPATH)
    if emprestimo_button:
        emprestimo_button.click()
        print(f"Formulário de emprestimo preenchido com: Título={titulo}, Código={cliente}, Data de emprestimo={data_emprestimo}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source)
# End funcionts for bot input forms

def main():

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    # bot.browse("https://www.botcity.dev")

    autor_form = "IFAM DX"
    preencher_formulario_autor(bot, autor_form)
    livro_titulo = "Programação Orientada a Objetos"
    livro_codigo = "POO"
    preencher_formulario_livro(bot, livro_titulo, livro_codigo)

    biblioteca_nome = "IFAM"
    preencher_formulario_biblioteca(bot, biblioteca_nome)

    titulo_livro = "Programação Orientada a Objetos"
    cliente = "Fulano da Silva"
    data_emprestimo = "02-02-2024"
    preencher_formulario_emprestimo(bot, titulo_livro, cliente, data_emprestimo)

    bot.wait(3000)
    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()