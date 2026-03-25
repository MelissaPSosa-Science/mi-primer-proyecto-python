#Capa para para hacer pruebas locales
from handler import lambda_handler

evento_prueba = {
    "nombre": "Luis"
}

resultado = lambda_handler(evento_prueba, None)
print(resultado)