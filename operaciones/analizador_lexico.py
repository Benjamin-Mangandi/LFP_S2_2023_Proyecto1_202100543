from objetos import aritmetica
from objetos import estilo
from objetos import errores
import json
def analizar_palabra(abecedario, palabra,numero,columna, fila):
    for letra in palabra:
        if letra not in abecedario:
            nuevo_error = errores.formato_error(numero,letra,"Error Lexico", columna, fila)

errores_validados = {"Errores":[
]}
datos_validados = []
datos_estilo = []
inicio2 = ["valor1", "valor2"]
inicio = ["operaciones", "configuraciones", "operacion"]
abecedario = ["{","}","[","]", ":", ",", '"' , " ", "\n" ,"=" ,"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3","4", "5", "6", "7", "8", "9"]
operaciones_aritmeticas = ["suma", "resta",
                           "multiplicacion", "division", "potencia"]

def analizar(texto):
    num_error=0
    nuevo_texto=texto
    columna =1
    fila = 0
    posicion=0
    while errores_validados["Errores"]:
        errores_validados["Errores"].pop()
    for letra in texto:
        fila=fila+1
        if letra =="\n":
            columna=columna+1
            fila=0
        if letra.lower() not in abecedario:
            nuevo_texto = nuevo_texto.replace(letra, "")
            num_error=num_error+1
            nuevo_error = errores.formato_error(num_error,letra,"Error Lexico", columna, fila)
            errores_validados["Errores"].append(
                {
                    "No": num_error,
                    "Descripcion": {
                        "lexema": letra,
                        "tipo": "error lexico",
                        "columna": columna,
                        "fila": fila
                    }
                }
            )
            posicion=posicion+1
    print(nuevo_texto)
    datos = json.loads(nuevo_texto)
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
                            num_error=num_error+1
                            analizar_palabra(abecedario, nombre, num_error,i,i)
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
            num_error=num_error+1
            analizar_palabra(abecedario,configuracion.lower(),num_error,i,i)
            break