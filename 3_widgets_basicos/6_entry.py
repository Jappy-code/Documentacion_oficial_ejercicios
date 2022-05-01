import re
from tkinter import *
from tkinter import ttk

root = Tk()

username = StringVar()
name = ttk.Entry(root, textvariable=username, width=20, show='*')
name.grid(column=0, row=0, padx=20, pady=20)
name.focus()

root.mainloop()





"""
Entry/Entrada
Un widget de entrada presenta a los usuarios un campo de texto de una sola línea donde pueden escribir un valor de cadena. Estos pueden ser casi cualquier cosa: un nombre, una ciudad, una contraseña, número de seguro social, etc.


Las entradas se crean usando la ttk.Entry clase:
        username = StringVar()
        name = ttk.Entry(parent, textvariable=username)

Se width puede especificar una opción de configuración para proporcionar el número de caracteres que debe tener la entrada. Esto le permite, por ejemplo, mostrar una entrada más corta para un código postal.
"""


"""
Contenido de la entrada

Hemos visto cómo los widgets de botón de control y botón de radio tienen un valor asociado a ellos. Las entradas también lo hacen, y normalmente se accede a ese valor a través de una variable vinculada especificada por la textvariable opción de configuración.

        A diferencia de los diversos botones, las entradas no tienen un texto o una imagen junto a ellas para identificarlas. Use un widget de etiqueta separado para eso.


También puede obtener o cambiar el valor del widget de entrada sin pasar por la variable vinculada. El getmétodo devuelve el valor actual, y los métodos deletey insertle permiten cambiar el contenido, por ejemplo

        name.delete(0,'end')          # delete between two indices, 0-based
        name.insert(0, 'your name')   # insert new text at a given index
"""



"""
contraseñas

Las entradas se pueden usar para contraseñas, donde los contenidos reales se muestran como una viñeta u otro símbolo. Para hacer esto, establezca la showopción de configuración en el carácter que le gustaría mostrar.
"""


"""
Estados de widgets

Al igual que los diversos botones, las entradas también se pueden desactivar mediante el statecomando (y se pueden consultar con instate). Las entradas también pueden usar la bandera del estado readonly; si se establece, los usuarios no pueden cambiar la entrada, aunque aún pueden seleccionar el texto que contiene (y copiarlo en el portapapeles). También hay un invalid estado, establecido si el widget de entrada falla en la validación, lo que nos lleva a...
"""