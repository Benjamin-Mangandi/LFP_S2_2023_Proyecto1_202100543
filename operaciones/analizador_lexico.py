from objetos import aritmetica
from objetos import estilo
from operaciones import graficador
import tkinter
import json

errores_validados = {"Errores": [
]}
datos_validados = []
datos_estilo = []
inicio_3 = ["fuente", "texto", "forma", "fondo"]
inicio2 = ["valor1", "valor2", "operacion", "operación"]
inicio = ["operaciones", "configuraciones"]
abecedario = ["{", "}", "[", "]", ":", ",", '"', " ", "\n", "=", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2",
              "3", "4", "5", "6", "7", "8", "9", ".", "-", "á", "é", "í", "ó", "ú"]
operaciones_aritmeticas = ["suma", "resta",
                           "multiplicacion", "division", "potencia", "mod",
                           "seno", "raiz", "inverso", "coseno", "tangente"]


def sub_operaciones(i, j, arreglo, configuracion, valor):
    for dato in arreglo[configuracion][i][valor]:
        errores_2 = 0
        nombres_2 = 0
        nombres_2 = dato.keys()
        for nombre in nombres_2:
            if nombre not in inicio2:
                errores_2 = errores_2+1
                break
            else:
                continue
        if errores_2 > 0:
            return "Error"
        if len(nombres_2) == 2:
            sub_operacion = arreglo[configuracion][i][valor][j]["operacion"]
            if isinstance(arreglo[configuracion][i][valor][j]["valor1"], list):
                sub_valor1 = sub_sub_operaciones(
                    i, j, arreglo, configuracion, valor, "valor1")
            else:
                sub_valor1 = arreglo[configuracion][i][valor][j]["valor1"]
            return aritmetica.operacion.operar(sub_operacion, sub_valor1, 1)
        if len(nombres_2) == 3:
            sub_operacion = arreglo[configuracion][i][valor][j]["operacion"]
            if isinstance(arreglo[configuracion][i][valor][j]["valor1"], list):
                sub_valor1 = sub_sub_operaciones(
                    i, j, arreglo, configuracion, valor, "valor1")
            else:
                sub_valor1 = arreglo[configuracion][i][valor][j]["valor1"]
            if isinstance(arreglo[configuracion][i][valor][j]["valor2"], list):
                sub_valor2 = sub_sub_operaciones(
                    i, j, arreglo, configuracion, valor, "valor2")
            else:
                sub_valor2 = arreglo[configuracion][i][valor][j]["valor2"]
            return aritmetica.operacion.operar(sub_operacion, sub_valor1, sub_valor2)


def sub_sub_operaciones(i, j, arreglo, configuracion, valor, valor2):
    k = 0
    for dato in arreglo[configuracion][i][valor][j][valor2]:
        errores_3 = 0
        nombres_3 = 0
        nombres_3 = dato.keys()
        for nombre in nombres_3:
            if nombre not in inicio2:
                errores_3 = errores_3+1
                break
            else:
                continue
        if errores_3 > 0:
            return "Error"
        if len(nombres_3) == 2:
            sub_operacion = arreglo[configuracion][i][valor][j][valor2][k]["operacion"]
            if isinstance(arreglo[configuracion][i][valor][j][valor2][k]["valor1"], list):
                nuevo_valor1 = 1
                return nuevo_valor1
            else:
                sub_valor1 = arreglo[configuracion][i][valor][j][valor2][k]["valor1"]
            return aritmetica.operacion.operar(sub_operacion, sub_valor1, 1)
        if len(nombres_3) == 3:
            sub_operacion = arreglo[configuracion][i][valor][j][valor2][k]["operacion"]
            if isinstance(arreglo[configuracion][i][valor][j][valor2][k]["valor1"], list):
                nuevo_valor1 = 1
                return nuevo_valor1
            else:
                sub_valor1 = arreglo[configuracion][i][valor][j][valor2][k]["valor1"]
            if isinstance(arreglo[configuracion][i][valor][j][valor2][k]["valor2"], list):
                sub_valor2 = 1
            else:
                sub_valor2 = arreglo[configuracion][i][valor][j][valor2][k]["valor2"]
            return aritmetica.operacion.operar(sub_operacion, sub_valor2, sub_valor1)


def analizar(texto):
    graficador.reiniciar()
    num_error = 0
    nuevo_texto = texto
    columna = 1
    fila = 0
    posicion = 0
    while errores_validados["Errores"]:
        errores_validados["Errores"].pop()
    for letra in texto:
        fila = fila+1
        if letra == "\n":
            columna = columna+1
            fila = 0
        if letra.lower() not in abecedario:
            nuevo_texto = nuevo_texto.replace(letra, "")
            num_error = num_error+1
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
            posicion = posicion+1
    try:
        datos = json.loads(nuevo_texto)
        with open("archivo.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        with open("archivo.json", "r") as archivo:
            datos_ingresados = json.load(archivo)
    except json.JSONDecodeError:
        notificacion = tkinter.Toplevel()
        notificacion.title("Alerta")
        notificacion.geometry("400x150")
        etiqueta = tkinter.Label(
            notificacion, text="El archivo no contiene datos o tiene un formato incorrecto")
        etiqueta.pack(padx=20, pady=20)
        boton_cerrar = tkinter.Button(
            notificacion, background="#FF1919", text="Cerrar", command=notificacion.destroy)
        boton_cerrar.pack(pady=10)
        boton_cerrar.config(height=2, width=10)
        return
    contador = 0
    i = 0
    atributos = datos_ingresados["configuraciones"][0].keys()
    errores_estilo = 0
    for atributo in atributos:
        if atributo not in inicio_3:
            errores_estilo = errores_estilo+1
            break
        else:
            continue
    if errores_estilo <= 0:
        nuevo_texto = datos_ingresados["configuraciones"][0]["texto"]
        nuevo_fondo = datos_ingresados["configuraciones"][0]["fondo"]
        nueva_fuente = datos_ingresados["configuraciones"][0]["fuente"]
        nueva_forma = datos_ingresados["configuraciones"][0]["forma"]
        nuevo_estilo = estilo.estilo_grafico(
            nuevo_texto, nuevo_fondo, nueva_fuente, nueva_forma)
        datos_estilo.append(nuevo_estilo)
    else:
        nuevo_texto = "Operaciones"
        nuevo_fondo = "White"
        nueva_fuente = "black"
        nueva_forma = "circle"
        nuevo_estilo = estilo.estilo_grafico(
            nuevo_texto, nuevo_fondo, nueva_fuente, nueva_forma)
        datos_estilo.append(nuevo_estilo)
    for configuracion in datos_ingresados:
        if configuracion.lower() == "operaciones":
            for tipo in datos_ingresados["operaciones"]:
                errores = 0
                nombres = 0
                nombres = tipo.keys()
                for nombre in nombres:
                    if nombre not in inicio2:
                        errores = errores+1
                        break
                    else:
                        continue
                if errores > 0:
                    i = i+1
                    continue
                if len(nombres) == 2:
                    nueva_operacion = datos_ingresados[configuracion][i]["operacion"].lower(
                    )
                    if isinstance(datos_ingresados[configuracion][i]["valor1"], list):
                        j = 0
                        nuevo_valor1 = sub_operaciones(
                            i, j, datos_ingresados, configuracion, "valor1")
                        if nuevo_valor1 == "Error":
                            break
                    else:
                        nuevo_valor1 = datos_ingresados[configuracion][i]["valor1"]
                    resultado = aritmetica.operacion.operar(
                        nueva_operacion, nuevo_valor1, 1)
                    nuevo_dato = aritmetica.operacion(nueva_operacion, round(
                        nuevo_valor1, 4), 1, round(resultado, 4))
                    datos_validados.append(nuevo_dato)
                    graficador.crear_nodo(
                        datos_validados, contador, 1, nuevo_estilo)
                    contador = contador+1
                    i = i+1
                elif len(nombres) == 3:
                    nueva_operacion = datos_ingresados[configuracion][i]["operacion"].lower(
                    )
                    if isinstance(datos_ingresados[configuracion][i]["valor1"], list):
                        j = 0
                        nuevo_valor1 = sub_operaciones(
                            i, j, datos_ingresados, configuracion, "valor1")
                        if nuevo_valor1 == "Error":
                            break
                    else:
                        nuevo_valor1 = datos_ingresados[configuracion][i]["valor1"]
                    if isinstance(datos_ingresados[configuracion][i]["valor2"], list):
                        j = 0
                        nuevo_valor2 = sub_operaciones(
                            i, j, datos_ingresados, configuracion, "valor2")
                        if nuevo_valor2 == "Error":
                            break
                    else:
                        nuevo_valor2 = datos_ingresados[configuracion][i]["valor2"]
                    resultado = aritmetica.operacion.operar(
                        nueva_operacion, nuevo_valor1, nuevo_valor2)
                    nuevo_dato = aritmetica.operacion(nueva_operacion, round(
                        nuevo_valor1, 4), round(nuevo_valor2, 4), round(resultado, 4))
                    datos_validados.append(nuevo_dato)
                    graficador.crear_nodo(
                        datos_validados, contador, 0, nuevo_estilo)
                    contador = contador+1
                    i = i+1
    if len(errores_validados["Errores"]) < 1:
        notificacion = tkinter.Toplevel()
        notificacion.title("Completado")
        notificacion.geometry("400x150")
        etiqueta = tkinter.Label(
            notificacion, text="Archivo analizado con Exito, no se han encontrado errores")
        etiqueta.pack(padx=20, pady=20)
        boton_cerrar = tkinter.Button(
            notificacion, background="#FF1919", text="Cerrar", command=notificacion.destroy)
        boton_cerrar.pack(pady=10)
        boton_cerrar.config(height=2, width=10)
    else:
        notificacion = tkinter.Toplevel()
        notificacion.title("Completado - ALERTA")
        notificacion.geometry("650x150")
        etiqueta = tkinter.Label(
            notificacion, text="Se ha completado el analisis; errores encontrados, por favor pulse el botón 'Ver Errores' para más información")
        etiqueta.pack(padx=20, pady=20)
        boton_cerrar = tkinter.Button(
            notificacion, background="#FF1919", text="Cerrar", command=notificacion.destroy)
        boton_cerrar.pack(pady=10)
        boton_cerrar.config(height=2, width=10)
