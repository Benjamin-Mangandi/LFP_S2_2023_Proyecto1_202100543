from graphviz import Digraph
from operaciones import analizador_lexico as AL
dot = Digraph(comment='Grafico')
def reiniciar():
     dot.clear()
def graficar(datos):
    dot.render(datos[0].texto, view=True)
def crear_nodo(datos, i, reconocedor):
        if reconocedor == 1:
             dot.node("tipo"+str(i), str(datos[i].tipo)+" \n "+str(datos[i].resultado))
             dot.node('valor1'+str(i), str(datos[i].valor1))
             dot.edge('tipo'+str(i), 'valor1'+str(i), label='')
        else:
             dot.node("tipo"+str(i), str(datos[i].tipo)+" \n "+str(datos[i].resultado))
             dot.node('valor1'+str(i), str(datos[i].valor1))
             dot.node('valor2'+str(i), str(datos[i].valor2))
             dot.edge('tipo'+str(i), 'valor1'+str(i), label='')
             dot.edge('tipo'+str(i), 'valor2'+str(i), label='')
def agregar_estilo(contador, datos_estilo):
    for i in range(contador):
        dot.node("tipo"+str(i),style="filled", shape=datos_estilo.forma, 
                 fillcolor=datos_estilo.fondo, fontcolor=datos_estilo.fuente)
        dot.node('valor1'+str(i),style="filled", shape=datos_estilo.forma, 
                 fillcolor=datos_estilo.fondo, fontcolor=datos_estilo.fuente)
        dot.node('valor2'+str(i),style="filled", shape=datos_estilo.forma, 
                 fillcolor=datos_estilo.fondo, fontcolor=datos_estilo.fuente)