#Simulacion de una base de datos

def buscar_usuario(nombre):
    usuarios = {
        "Melissa": "Bienvenida de nuevo, Melissa",
        "Ana": "Hola Ana, qué gusto verte",
        "Luis": "Hola Luis, bienvenido"
    }

    return usuarios.get(nombre)