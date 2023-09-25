# **Lenguajes Formales y de Programación**
## *Primer Proyecto*
### **Segundo Semestre 2023**

```js
Universidad San Carlos De Guatemala
Programador: Harold Benjamin Oxlaj Mangandi
Carne: 202100543
Lenguaje: Python
Bibliotecas usadas: graphviz, json, tkinter, subprocess, graphviz, math
```
---
### Descripción del Proyecto
El siguiente proyecto es un analizador lexico, el cual tiene como objetivo reconocer errores lexico ingresados por el usuario haciendo uso del formato .json, mostrarle al usuario los posibles errores al momento de leer un archivo y graficar las operaciones ingresadas por medio de nodos utilizando para eso la libreria graphiz.
## Partes del Proyecto
### **Archivos y Carpetas**
### Carpeta Principal
# main.py
**Importa**: *analizador_lexico, graficador*
Es en donde se encuentra el iniciador de la ventana principal: *menu*, contiene todos los elementos de tkinter de la ventana principal, la cual cuenta con un cuadro de texto por medio de *tkinter.text* el cual sirve para que el usuario ingrese las operaciones deseadas o bien cargue un archivo mediante el boton *abrir* el cual está como comando en un *tkinter.Menu*; se puede sobreescribir el archivo, guardarlo como otro diferente o salir de la aplicacion
![main](https://i.ibb.co/Yy8rpyd/menu1.png)
![main2](https://i.ibb.co/DYd09Rg/menu2.png)
## **Funciones**
### *seleccionar_archivo*
**Parametros**: nombre del cuadro de texto
Esta función permite abrir un archivo de texto al usuario por medio de la función de tkinter 
*filedialog.askopenfilename()* inserta el texto en el cuadro de texto y reinicia los nodos anteriores si es que tuvieran datos de analisis anteriores por medio de la función *graficador.reiniciar()* y asigna la ruta a la variable *ruta_archivo*
![archivo](https://i.ibb.co/tBpNm9y/seleccionar-archivo.png)
### *guardar*
**Parametros**: nombre del cuadro de texto
Esta función permite o bien sobreescribir el archivo si es que existe o crear uno nuevo y guardarlo con el nombre que desee el usuario por medio de una validación de la variable *ruta_archivo*, si es que contiene la ruta de un archivo abierto.
![guardar](https://i.ibb.co/Qksqjkq/guardar.png)
### *guardar_como*
**Parametros**: nombre del cuadro de texto
Esta función permite guardar como un archivo aparte el texto que el usuario haya ingresado y le asigna la ruta a la variable *ruta_archivo*
### *salir*
Esta funcion simplemente cierra la ventana junto con el proceso con la funcion *destroy()*
![guardar_salir](https://i.ibb.co/fnnpsrD/guardar-como-y-salir.png)
### *buscando_errores*
**Parametros**: diccionario de errores
Esta funcion recibe como parametro un diccionario el cual contendra los errores del texto dentro de un arreglo, dependiendo la longitud del arreglo mostrará un mensaje de que no hay ningun error, o creará un archivo .json con los errores y lo abrirá con el bloc de notas.
![buscando_errores](https://i.ibb.co/NtS74XV/buscando-errores.png)
### *reporte_documento*
Esta funcion determina si hay operaciones ingresadas por el usuario por medio de una condicion con la varible del archivo **analizador_lexico** *datos_validados* si los hay grafica normalmente, si no, manda una advertencia al usuario.
![reporte](https://i.ibb.co/RQwqTQ8/reporte-documento.png)
### *manual_usuario y manual_tecnico*
Estas funciones simplemente abren en el bloc de notas los archivos del manual de usuario y tecnico respectivamente
![usuario_tecnico](https://i.ibb.co/M71RbzX/usuario-tecnico.png)
### Operaciones
# analizador.py
## **Funciones**
### *analizar_palabra*
![analizar_palabra](https://i.ibb.co/Lxy3mJs/operacion.png)
### *sub_operaciones*
![sub_operaciones](https://i.ibb.co/Lxy3mJs/operacion.png)
### *sub_sub_operaciones*
![sub2_operaciones](https://i.ibb.co/Lxy3mJs/operacion.png)
### *analizar*
![analizar](https://i.ibb.co/Lxy3mJs/operacion.png)
# graficador.py
### *reiniciar*
Esta funcion simplemente reinicia los nodos ya creados en analisis anteriores por medio de *clear()*
### *graficar*
**Parametros**: arreglo
Esta funcion grafica los nodos creados por medio de la funcion *render()* y le da nombre al documento por medio del parametro ingresado que es en donde se guardan los datos del estilo en la posicion 0 y lo abre en un archivo pdf
![reiniciar y graficar](https://i.ibb.co/fFzns3y/reinicar-graficar.png)
### *crear_nodo*
**Parametros**: arreglo, numero, clave_numerica, varible de tipo estilo.
esta funcion crea y le da el estilo a los nodos, tiene una condicion con la clave numerica, si es igual a 1 es que solo se crean 2 nodos para esa operacion por medio de una funcion *node()* y la funcion *edge()* para unirlos, si es 0, se hacen 3 nodos para una operacion con su respectivo estilo.
![crear_nodo](https://i.ibb.co/fXVDPYF/crear-nodo.png)
## **Funciones**
### objetos
# aritmetica.py
# **Clase**: operacion
Esta clase tiene como atributos *tipo*, que es tipo de operación aritmetica, *valor1*, que es el primer valor ingresado, *valor2* que es el segundo valor ingresado, *resultado* que es el resultado de la operacion aritmetica dado los dos valores.
![operacion](https://i.ibb.co/Lxy3mJs/operacion.png)
## **Funciones**
### *operar*
**Parametros**: tipo de operacion, valor 1 y valor2
Esta funcion opera los dos valores ingresados teniendo como condición el tipo de operacion, por ejemplo, si el tipo de operación es "suma" suma los dos valores, o si es division, divide los dos valores asegurandose que no sea 0 el segundo.
Redondea todas las operaciones a 4 decimales.
![operar1](https://i.ibb.co/JR9T6dX/operar1.png)
![operar2](https://i.ibb.co/27XQjDx/operar2.png)
![operar3](https://i.ibb.co/ryngrCr/operar3.png)
![operar4](https://i.ibb.co/gd0dNQk/operar4.png)
# estilo.py
# **Clase**: estilo_grafico
Esta clase tiene como atributos *texto*, que es el nombre que se le dará al documento, *fondo*, que es color de los nodos, *fuente*, que es color de la letra y *forma* que es la forma que tendra los nodos.
![estilo_grafico](https://i.ibb.co/3RBPfrC/estilo-grafico.png)
