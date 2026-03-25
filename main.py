#Este main actua como la entrada de una lambda
#ejecuta lo servicios

from servicio import saludar
import repositorio

##Definicion de una funcion tipo Lambda AWS

#Esta es la función principal que AWS Lambda normalmente ejecuta
#event   --> los datos que llegan
#context --> informacion extra de la Lambda
def lambda_handler(event, context):
    nombre = event["nombre"]               #Se obtiene un dato del evento, en este caso el nombre
    respuesta = saludar(nombre,repositorio)            #Aqui estoy llamando la lógica del negocio, en este caso la función saludar que defini en servicos

    return {                               #Aqui estoy regresando mi respuesta en formato JSON 
        "statusCode": 200,
        "body": respuesta
    }

#Pasos extra para no usar AWS
evento_prueba = {
    "nombre": "Melissa"
}

#Ejecución de la Lambda falsa
resultado = lambda_handler(evento_prueba, None)
print(resultado)