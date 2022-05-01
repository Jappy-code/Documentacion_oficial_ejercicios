from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Label/etiqueta")

mainframe = ttk.Frame(root).grid(column=0, row=0)

label = ttk.Label(mainframe, text="Label/Etiqueta 1")
label.grid(column=0, row=0)

resultContens = StringVar()
resultContens.set("Label/etiqueta 1 - con una variable asignada")
label['textvariable'] = resultContens

root.mainloop()


"""
Label/etiqueta

Una etiqueta es un widget que muestra texto o imágenes, por lo general, que los usuarios solo verán pero con los que no interactuarán. Las etiquetas se utilizan para identificar controles u otras partes de la interfaz de usuario, proporcionar comentarios o resultados textuales, etc.


Las etiquetas se crean usando la ttk.Labelclase. A menudo, el texto o la imagen que mostrará la etiqueta se especifican a través de las opciones de configuración al mismo tiempo:

    label = ttk.Label(parent, text='Full name:')


Al igual que los marcos, las etiquetas pueden tener varias opciones de configuración diferentes, lo que puede alterar la forma en que se muestran.
"""



"""
Mostrar texto

La textopción de configuración (mostrada arriba al crear la etiqueta) es la más utilizada, particularmente cuando la etiqueta es puramente decorativa o explicativa. Puede cambiar qué texto se muestra modificando esta opción de configuración. Esto se puede hacer en cualquier momento, no solo cuando se crea la etiqueta por primera vez.

También puede hacer que el widget controle una variable en su secuencia de comandos. Cada vez que cambie la variable, la etiqueta mostrará el nuevo valor de la variable. Esto se hace con la textvariable opción:

    resultsContents = StringVar()
    label['textvariable'] = resultsContents
    resultsContents.set('New value to display')


Tkinter solo le permite adjuntar widgets a una instancia de la StringVar clase, pero no variables arbitrarias de Python. Esta clase contiene toda la lógica para observar los cambios y comunicarlos entre la variable y Tk. Utilice los métodos get y set para leer o escribir el valor actual de la variable.
"""