import graphviz
import tkinter
menu = tkinter.Tk()
menu.geometry("800x600")
menu.config(bg="green")
analizar_boton = tkinter.Button(menu, text="Analizar Texto")
analizar_boton.grid(column=0, row=0, padx=40, pady=5)
errores_boton = tkinter.Button(menu, text="Ver Errores")
errores_boton.grid(column=1, row=0, padx=40, pady=5)
menu.mainloop()