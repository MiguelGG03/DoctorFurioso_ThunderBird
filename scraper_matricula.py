"""
Este script es un ejemplo de cómo usar BeautifulSoup y expresiones regulares para buscar matrículas de coche en un archivo de texto.
"""
from bs4 import BeautifulSoup
import re

with open('thundebird\ccnsqul8.default\Mail\pop-mail.outlook.com\Inbox') as file:
    soup = BeautifulSoup(file, 'html.parser')
    # Expresión regular para una matrícula de coche genérica
    # Este patrón es solo un ejemplo y debe ser ajustado a lo que necesitas
    patron_matricula = r"\b[A-Z0-9]{6,8}-[A-Z]\b"

    # Buscar todas las ocurrencias del patrón en el texto
    matriculas_encontradas = re.findall(patron_matricula, soup.get_text())

    # Imprimir las matrículas encontradas
    for matricula in matriculas_encontradas:
        print(matricula)

