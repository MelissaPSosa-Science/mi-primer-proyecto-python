#Este main actua como la entrada de una lambda
#Ejecuta lo servicios

from servicio import saludar
import repo_memoria as repo

##Definicion de una funcion tipo Lambda AWS

#Esta es la función principal que AWS Lambda normalmente ejecuta
#event   --> los datos que llegan
#context --> informacion extra de la Lambda
def lambda_handler(event, context):
    try:
        nombre = event["nombre"]               #Se obtiene un dato del evento, en este caso el nombre
        respuesta = saludar(nombre,repo)       #Aqui estoy llamando la lógica del negocio, en este caso la función saludar que defini en servicos

        return {                               #Aqui estoy regresando mi respuesta en formato JSON 
            "statusCode": 200,
            "body": respuesta
        }
    except Exception as e:
        return {
            "statusCode":400,
            "body": str(e)
        }
