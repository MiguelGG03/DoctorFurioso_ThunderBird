"""
Extraer el color del coche de un correo electrónico
"""
from bs4 import BeautifulSoup
import re

with open('thundebird\ccnsqul8.default\Mail\pop-mail.outlook.com\Inbox') as file:
    soup = BeautifulSoup(file, 'html.parser')
    # Expresión regular para buscar el color del coche
    patron_color = r"Color: (.+)"
    resultado_color = re.search(patron_color, soup.get_text())

    # Extraer el color si se encontró en el texto
    color_coche = resultado_color.group(1) if resultado_color else "No encontrado"

    print(color_coche)