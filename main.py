import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from operaciones import graficador
from operaciones import analizador_lexico
import json
import subprocess


def seleccionar_archivo(cuadro_texto):
    archivo = filedialog.askopenfilename(title="Seleccionar un archivo")
    with open(archivo, "r") as archivo_cargado:
        texto = archivo_cargado.read()
    cuadro_texto.delete(1.0, END)
    cuadro_texto.insert(1.0, texto)
    ruta_archivo.set(archivo)
    graficador.reiniciar()
def guardar(cuadro_texto):
    if ruta_archivo.get() == "":
        texto = cuadro_texto.get("1.0", END)
        archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo_guardado:
            with open(archivo_guardado, "w") as archivo:
                archivo.write(texto)
    else:
        try:
            texto = cuadro_texto.get("1.0", END)
            with open(ruta_archivo.get(), "w") as archivo:
                archivo.write(texto)
        except Exception:
            print("no se pudo guardar el archivo")
def guardar_como (cuadro_texto):
    texto = cuadro_texto.get("1.0", END)
    archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo_guardado:
        with open(archivo_guardado, "w") as archivo:
            archivo.write(texto)
    ruta_archivo.set(archivo)
def salir():
    menu.destroy()


def buscando_errores(errores):
    if len(errores["Errores"]) < 1:
        notificacion = tkinter.Toplevel()
        notificacion.title("Alerta")
        notificacion.geometry("400x150")
        etiqueta = tkinter.Label(notificacion, text="No se han encontrado errores o aún no ha analizado el archivo.")
        etiqueta.pack(padx=20, pady=20)
        boton_cerrar = tkinter.Button(notificacion, background="#FF1919",text="Cerrar", command=notificacion.destroy)
        boton_cerrar.pack(pady=10)
        boton_cerrar.config(height=2,width=10)
    else:
        with open("RESULTADOS_202100543.json", "w") as archivo:
            json.dump(analizador_lexico.errores_validados, archivo, indent=4)
        subprocess.Popen(['notepad.exe', "RESULTADOS_202100543.json"])
def reporte_documento():
    graficador.graficar(analizador_lexico.datos_estilo)

menu = tkinter.Tk()
menu.geometry("800x600", )
menu.config(bg="#262732")
menu.title("Analizador Lexico")
opciones = ("abrir", "Guardar", "Guardar Como", "Salir")
frame_botones = tkinter.Frame(menu, background="#3D3D3F")
frame_botones.pack(side="top", fill="x")
barra_de_opciones = tkinter.Menu(menu)
opciones_archivo = tkinter.Menu(barra_de_opciones, tearoff=0)
opciones_archivo.add_command(label="Abrir", command=lambda: seleccionar_archivo(cuadro_de_texto))
opciones_archivo.add_command(label="Guardar", command=lambda: guardar(cuadro_de_texto))
opciones_archivo.add_command(label="Guardar Como", command=lambda: guardar_como(cuadro_de_texto))
opciones_archivo.add_command(label="Salir", command=salir)
analizar_boton = tkinter.Button(
    frame_botones, background="#0ECA19", height=2,width=13 ,text="Analizar Texto", command=lambda: analizador_lexico.analizar(cuadro_de_texto.get("1.0", END)))
errores_boton = tkinter.Button(
    frame_botones, background="#0ECA19",height=2,width=13, text="Ver Errores", command=lambda: buscando_errores(analizador_lexico.errores_validados))
reporte_boton = tkinter.Button(
    frame_botones, background="#0ECA19",height=2,width=13, text="Reporte", command=reporte_documento)
cuadro_de_texto = tkinter.Text(menu)
analizar_boton.pack(side="left", padx=80, pady=15)
errores_boton.pack(side="left", padx=80, pady=15)
reporte_boton.pack(side="left", padx=80, pady=15)
cuadro_de_texto.pack(side="left", padx=70)
barra_de_opciones.add_cascade(label="Archivo", menu=opciones_archivo)
ruta_archivo = tkinter.StringVar()
menu.config(menu=barra_de_opciones)
menu.resizable(False, False)
menu.mainloop()
