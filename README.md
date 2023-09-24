# **Lenguajes Formales y de Programación**
## *Primer Proyecto*
### **Segundo Semestre 2023**

```js
Universidad San Carlos De Guatemala
Programador: Harold Benjamin Oxlaj Mangandi
Carne: 202100543
Lenguaje: Python
Bibliotecas usadas: graphviz, json, tkinter, subprocess,graphviz, math
```
---
### Descripción del Proyecto
El siguiente proyecto es un analizador lexico, el cual tiene como objetivo reconocer errores lexico ingresados por el usuario haciendo uso del formato .json, mostrarle al usuario los posibles errores al momento de leer un archivo y graficar las operaciones ingresadas por medio de nodos utilizando para eso la libreria graphiz.
### Partes del Proyecto
## **Archivos y Carpetas**
## Carpeta Principal
# main.py
**Importa**: *analizador_lexico, graficador*
Es en donde se encuentra el iniciador de la ventana principal: *menu*, contiene todos los elementos de tkinter de la ventana principal, la cual cuenta con un cuadro de texto por medio de *tkinter.text* el cual sirve para que el usuario ingrese las operaciones deseadas o bien cargue un archivo mediante el boton *abrir* el cual está como comando en un *tkinter.Menu*; se puede sobreescribir el archivo, guardarlo como otro diferente o salir de la aplicacion
![main](https://i.ibb.co/85dsk2Q/menu.png)
# **Funciones**
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
![buscando_errores](https://i.ibb.co/NtS74XV/buscando-errores.png)
### *reporte_documento*
Esta funcion determina si hay operaciones ingresadas por el usuario por medio de una condicion con la varible del archivo **analizador_lexico** *datos_validados* si los hay grafica normalmente, si no, manda una advertencia al usuario.
![reporte](https://i.ibb.co/RQwqTQ8/reporte-documento.png)
### *manual_usuario y manual_tecnico*
Estas funciones simplemente abren en el bloc de notas los archivos del manual de usuario y tecnico respectivamente
![usuario_tecnico](https://i.ibb.co/M71RbzX/usuario-tecnico.png)
## Operaciones
# analizador.py
# **Funciones**
### *analizar_palabra*
### *sub_operaciones*
### *sub_sub_operaciones*
### *analizar*
# graficador.py
### *reiniciar*
### *graficar*
### *crear_nodo*
### *agregar_estilo*
# **Funciones**
## objetos
# aritmertica.py
# **Clase**: operacion
Esta clase tiene como atributos *tipo*, que es tipo de operación aritmetica, *valor1*, que es el primer valor ingresado, *valor2* que es el segundo valor ingresado, *resultado* que es el resultado de la operacion aritmetica dado los dos valores.
![operacion](https://i.ibb.co/Lxy3mJs/operacion.png)
# **Funciones**
### *operar*
**Parametros**: tipo de operacion, valor 1 y valor2
Esta funcion opera los dos valores ingresados teniendo como condición el tipo de operacion, por ejemplo, si el tipo de operación es "suma" suma los dos valores, o si es division, divide los dos valores asegurandose que no sea 0 el segundo.
Redondea todas las operaciones a 4 decimales.
![operar1](https://i.ibb.co/JR9T6dX/operar1.png)
![operar2](https://i.ibb.co/27XQjDx/operar2.png)
![operar3](https://i.ibb.co/ryngrCr/operar3.png)
![operar4](https://i.ibb.co/gd0dNQk/operar4.png)
# errores.py
# **Clase**: formato_error
Esta clase tiene como atributos *numero*, que es numero de error, *lexema*, que es el caracter que es reconocido como un error por el analizador, *tipo* que es el tipo de error, *columna* que es la columna donde se encuentra el error, *fila*, que es la fila donde se encuentra el error.
![formato_error](https://i.ibb.co/kcNGBgh/formato-error.png)
# estilo.py
# **Clase**: estilo_grafico
Esta clase tiene como atributos *texto*, que es el nombre que se le dará al documento, *fondo*, que es color de los nodos, *fuente*, que es color de la letra y *forma* que es la forma que tendra los nodos.
![estilo_grafico](https://i.ibb.co/3RBPfrC/estilo-grafico.png)
