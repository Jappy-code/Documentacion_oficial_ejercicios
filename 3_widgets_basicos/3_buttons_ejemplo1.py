from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Buttons/Bótones")

button1 = ttk.Button(root, text="Button de prueba")
button1.grid(column=0, row=0)

button1.state(['disabled'])     #establecer la bandera deshabilitada
button1.state(['!disabled'])    #borrar la bandera deshabilitada
button1.instate(['disabled'])   #verdadero si está deshabilitado, de lo contrario falso
button1.instate(['!disabled'])  #verdadero si no está deshabilitado, de lo contrario falso

root.mainloop()



"""
Por lo general, su contenido y la devolución de llamada de comando se especifican al mismo tiempo que se crea el botón. Al igual que con otros widgets, los botones aceptan varias opciones de configuración para modificar su apariencia y comportamiento, incluida la style opción estándar.
"""

"""
Texto o Imagen

Los botones toman las mismas opciones de configuración text, textvariable(raramente usadas), imagey como etiquetas. compoundEstos controlan si el botón muestra texto y/o una imagen

Los botones tienen una defaultopción de configuración. Si se especifica como active, esto le dice a Tk que el botón es el botón predeterminado en la interfaz de usuario; de lo contrario, es normal. Los botones predeterminados se invocan si los usuarios presionan la tecla Retorno o Intro. Algunas plataformas y estilos dibujarán este botón predeterminado con un borde o resaltado diferente. Tenga en cuenta que configurar esta opción no crea un enlace de evento que hará que la tecla Retorno o Intro active el botón; tienes que hacerlo tú mismo.
"""


"""
Estado del botón

Los botones y muchos otros widgets comienzan en un estado normal. Un botón responderá a los movimientos del mouse, se puede presionar e invocará su devolución de llamada de comando. Los botones también se pueden poner en un estado deshabilitado, donde el botón está atenuado, no responde a los movimientos del mouse y no se puede presionar. Su programa deshabilitaría el botón cuando su comando no sea aplicable en un momento dado.

Todos los widgets temáticos mantienen un estado interno, representado como una serie de banderas binarias. Cada bandera se puede activar (activar) o borrar (desactivar). Puede configurar o borrar estos indicadores diferentes y verificar la configuración actual usando los métodos state y instate. Los botones hacen uso de la disabled bandera para controlar si los usuarios pueden o no presionar el botón. Por ejemplo:

        b.state(['disabled'])          # set the disabled flag
        b.state(['!disabled'])         # clear the disabled flag
        b.instate(['disabled'])        # true if disabled, else false
        b.instate(['!disabled'])       # true if not disabled, else false
        b.instate(['!disabled'], cmd)  # execute 'cmd' if not disabled


La lista completa de indicadores de estado disponibles para los widgets temáticos es: active, disabled, focus, pressed, selected, background, readonly, alternate y invalid. Estos se describen en la referencia de widgets temáticos . Si bien todos los widgets tienen el mismo conjunto de indicadores de estado, no todos los estados son significativos para todos los widgets. También es posible volverse sofisticado con los métodos statey instatey especificar varias banderas de estado al mismo tiempo.
"""