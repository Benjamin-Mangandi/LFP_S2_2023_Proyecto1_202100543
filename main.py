import graphviz
import tkinter
from tkinter import ttk


def analizar():
    print("analizar")


def buscando_errores():
    print("Error")


def reporte_documento():
    print("Reporte")


menu = tkinter.Tk()
menu.geometry("800x600", )
menu.config(bg="#08227E")
menu.title("Reportes")
opciones = ("abrir", "Guardar", "Guardar Como", "Salir")
frame_botones = tkinter.Frame(menu, background="#0E74CA")
frame_botones.pack(side="top", fill="x")
opciones_boton = ttk.Combobox(
    frame_botones, background="#0ECA19", text="Archivo", values=opciones)
analizar_boton = tkinter.Button(
    frame_botones, background="#0ECA19", text="Analizar Texto", command=analizar)
errores_boton = tkinter.Button(
    frame_botones, background="#0ECA19", text="Ver Errores", command=buscando_errores)
reporte_boton = tkinter.Button(
    frame_botones, background="#0ECA19", text="Reporte", command=reporte_documento)
cuadro_de_texto = tkinter.Text(menu, wrap="word")
opciones_boton.pack(side="left", padx=50, pady=10)
reporte_boton.pack(side="left", padx=50, pady=10)
analizar_boton.pack(side="left", padx=50, pady=10)
errores_boton.pack(side="left", padx=50, pady=10)
cuadro_de_texto.pack(side="left", padx=70)
menu.mainloop()
