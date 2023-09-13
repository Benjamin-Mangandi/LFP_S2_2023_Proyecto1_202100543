import graphviz
import tkinter
from tkinter import *
from tkinter import ttk
from operaciones import analizador_lexico


def salir():
    menu.destroy()


def buscando_errores():
    print("Error")


def reporte_documento():
    print("Reporte")


menu = tkinter.Tk()
menu.geometry("800x600", )
menu.config(bg="#262732")
menu.title("Analizador Lexico")
opciones = ("abrir", "Guardar", "Guardar Como", "Salir")
frame_botones = tkinter.Frame(menu, background="#3D3D3F")
frame_botones.pack(side="top", fill="x")
barra_de_opciones = tkinter.Menu(menu)
opciones_archivo = tkinter.Menu(barra_de_opciones, tearoff=0)
opciones_archivo.add_command(label="Abrir")
opciones_archivo.add_command(label="Guardar")
opciones_archivo.add_command(label="Guardar Como")
opciones_archivo.add_command(label="Salir", command=salir)
analizar_boton = tkinter.Button(
    frame_botones, background="#0ECA19", height=2,width=13 ,text="Analizar Texto", command=lambda: analizador_lexico.analizar(cuadro_de_texto.get("1.0", END)))
errores_boton = tkinter.Button(
    frame_botones, background="#0ECA19",height=2,width=13, text="Ver Errores", command=buscando_errores)
reporte_boton = tkinter.Button(
    frame_botones, background="#0ECA19",height=2,width=13, text="Reporte", command=reporte_documento)
cuadro_de_texto = tkinter.Text(menu)
analizar_boton.pack(side="left", padx=80, pady=15)
errores_boton.pack(side="left", padx=80, pady=15)
reporte_boton.pack(side="left", padx=80, pady=15)
cuadro_de_texto.pack(side="left", padx=70)
barra_de_opciones.add_cascade(label="Archivo", menu=opciones_archivo)
menu.config(menu=barra_de_opciones)
menu.resizable(False, False)
menu.mainloop()
