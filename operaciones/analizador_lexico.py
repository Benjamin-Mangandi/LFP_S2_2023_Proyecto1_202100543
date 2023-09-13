import json
inicio = ["operaciones"]
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
sting = "sos"
operaciones_aritmeticas = ["suma", "resta", "multiplicacion", "division", "potencia"]
def analizar(texto):
    datos = json.loads(texto)
    with open("archivo.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    with open("archivo.json", "r") as archivo:
        datos_ingresados = json.load(archivo)
    for operacion in datos_ingresados:
        if operacion in inicio:
            for i in range (len(datos_ingresados["operaciones"])):
                operacion_objetivo = datos_ingresados[operacion][i]["operacion"]
                if operacion_objetivo.lower() in operaciones_aritmeticas:
                    print(datos_ingresados[operacion][i]["valor1"])