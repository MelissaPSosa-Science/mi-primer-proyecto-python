#Capa para para hacer pruebas locales
from handler import lambda_handler

evento_prueba = {
    "nombre": "Melissa"
}

resultado = lambda_handler(evento_prueba, None)
print(resultado)