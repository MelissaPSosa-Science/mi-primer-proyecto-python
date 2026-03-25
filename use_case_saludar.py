#Aqui debe ir la logica del negocio

#from repositorio import buscar_usuario

"""
def saludar(nombre):
    mensaje = buscar_usuario(nombre)

    if mensaje:
        return mensaje

    return f"Hola {nombre}"
"""

#Aqui inicia el servicio sin dependencia directa a la base de datos
def ejecutar(nombre, repo):
    mensaje = repo.buscar_usuario(nombre)

    if not mensaje:
        raise Exception(f"Usuario {nombre} no encontrado, no se encuentra en la base de datos")

    return mensaje