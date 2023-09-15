from objetos import aritmetica
from objetos import estilo
import json
def analizar_palabra(abecedario, palabra):
    for letra in palabra:
        if letra not in abecedario:
            print(letra)

datos_validados = []
datos_estilo = []
inicio2 = ["valor1", "valor2"]
inicio = ["operaciones", "configuraciones", "operacion"]
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
operaciones_aritmeticas = ["suma", "resta",
                           "multiplicacion", "division", "potencia"]


def analizar(texto):
    datos = json.loads(texto)
    with open("archivo.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    with open("archivo.json", "r") as archivo:
        datos_ingresados = json.load(archivo)
    i=0
    for configuracion in datos_ingresados:
        if configuracion.lower() in inicio:
            if configuracion.lower() == "operaciones":
                for tipo in datos_ingresados["operaciones"]:
                    nombres = 0
                    nombres = tipo.keys()
                    print(i)
                    for nombre in nombres:
                        if nombre in inicio2:
                            if nombre == "valor2":
                                nueva_operacion = datos_ingresados[configuracion][i]["operacion"]
                                nuevo_valor1 = datos_ingresados[configuracion][i]["valor1"]
                                nuevo_valor2 = datos_ingresados[configuracion][i]["valor2"]
                                nueva_operacion = aritmetica.operacion(nueva_operacion,nuevo_valor1, nuevo_valor2)
                                datos_validados.append(nueva_operacion)
                                i=i+1
                                break
                        elif nombre not in inicio:
                            analizar_palabra(abecedario, nombre)
                            i=i+1
                            break
                        


                        
    
            elif configuracion.lower() == "configuraciones":
                for i in range(len(datos_ingresados["configuraciones"])):
                    nuevo_texto = datos_ingresados[configuracion][i]["texto"]
                    nuevo_fondo = datos_ingresados[configuracion][i]["fondo"]
                    nueva_fuente = datos_ingresados[configuracion][i]["fuente"]
                    nueva_forma = datos_ingresados[configuracion][i]["forma"]
                    nuevo_estilo = estilo.estilo_grafico(nuevo_texto,nuevo_fondo, nueva_fuente, nueva_forma)
                    datos_estilo.append(nuevo_estilo)
        else:
            analizar_palabra(abecedario,configuracion.lower())
            break
    print(datos_validados)