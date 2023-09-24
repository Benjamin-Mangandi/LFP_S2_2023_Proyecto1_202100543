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
# __init__.py
## objetos
# aritmertica.py
### *operar*
# **Funciones**
# errores.py
# **Funciones**
# estilo.py
# **Funciones**


# **Funciones**

### *elegir_opcion*
![Codigo_opciones](https://i.ibb.co/L5m057m/elegir-opcion.png)

### *convertir_numericos*
![Codigo_numericos1](https://i.ibb.co/QCyWRxZ/convertir-numericos1.png)
![Codigo_numericos1](https://i.ibb.co/dWndjps/convertir-numericos2.png)

### *cargar_inventario*
![Codigo_inventario](https://i.ibb.co/QPS1sM4/cargar-inventario.png)

### *cargar_movimientos*
![Codigo_movimientos1](https://i.ibb.co/Ms4GsPY/cargar-movimientos1.png)
![Codigo_movimientos2](https://i.ibb.co/vVnXVrw/cargar-movimientos2.png)

### *crear_informe*
![Codigo_informe](https://i.ibb.co/tLVzQpy/creari-nforme.png)