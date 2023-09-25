from graphviz import Digraph
dot = Digraph(comment='Grafico')


def reiniciar():
    dot.clear()


def graficar(datos):
    dot.render(datos[0].texto, view=True)


def crear_nodo(datos, i, reconocedor, estilo):
    if reconocedor == 1:
        dot.node("tipo"+str(i), str(datos[i].tipo)+" \n "
                 + str(datos[i].resultado), style="filled", shape=estilo.forma,
                 fillcolor=estilo.fondo, fontcolor=estilo.fuente)
        dot.node('valor1'+str(i), str(datos[i].valor1), style="filled", shape=estilo.forma,
                 fillcolor=estilo.fondo, fontcolor=estilo.fuente)
        dot.edge('tipo'+str(i), 'valor1'+str(i), label='')
    else:
        dot.node("tipo"+str(i), str(datos[i].tipo)+" \n "+str(datos[i].resultado),
                 style="filled", shape=estilo.forma,
                 fillcolor=estilo.fondo, fontcolor=estilo.fuente)
        dot.node('valor1'+str(i), str(datos[i].valor1),
                 style="filled", shape=estilo.forma,
                 fillcolor=estilo.fondo, fontcolor=estilo.fuente)
        dot.node('valor2'+str(i), str(datos[i].valor2),
                 style="filled", shape=estilo.forma,
                 fillcolor=estilo.fondo, fontcolor=estilo.fuente)
        dot.edge('tipo'+str(i), 'valor1'+str(i), label='')
        dot.edge('tipo'+str(i), 'valor2'+str(i), label='')

