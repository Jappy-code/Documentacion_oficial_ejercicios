# frame traduce a marco en español
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Frame")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

mainframe['padding'] = (10, 45)  #/10 izquierda y derecha , 45 arriba y abajo
mainframe['borderwidth'] = 5
mainframe['relief'] = 'raised'
mainframe.grid_configure(padx=100, pady=50)


label1 = ttk.Label(mainframe, text="Hola mundo").grid()

root.mainloop()


"""
Tamaño solicitado

Por lo general, el tamaño de un marco está determinado por el tamaño y el diseño de los widgets que contiene. A su vez, esto está controlado por el administrador de geometría que administra los contenidos del marco en sí.

Si, por alguna razón, desea un marco vacío que no contenga otros widgets, puede establecer explícitamente su tamaño usando las opciones de configuración widthy/o height(de lo contrario, terminará con un marco muy pequeño).

Las distancias de pantalla, como el ancho y el alto, generalmente se especifican como una cantidad de píxeles. También puede especificarlos a través de uno de varios sufijos. Por ejemplo, 350significa 350 píxeles, 350c significa 350 centímetros, 350m significa 350 milímetros, 350i significa 350 pulgadas y 350p significa 350 puntos de impresora (1/72 de pulgada).
"""




"""
Relleno/padding

La padding opción de configuración se usa para solicitar espacio adicional alrededor del interior del widget. Si está colocando otros widgets dentro del marco, habrá un margen alrededor. Puede especificar el mismo relleno para todos los lados, diferente relleno horizontal y vertical, o relleno para cada lado por separado.

    mainframe = ttk.Frame(root, padding=("3 3 12 12")) / izquierda 3, arriba 3, derecha 12, abajo 12
    f['padding'] = 5           # 5 pixels on all sides / 5 píxeles en todos los lados 
    f['padding'] = (5,10)      # 5 on left and right, 10 on top and bottom / 5 a izquierda y derecha, 10 arriba y abajo
    f['padding'] = (5,7,10,12) # left: 5, top: 7, right: 10, bottom: 12 / izquierda 5, arriba 7, derecha 10, abajo 12
"""





"""
Borders/fronteras

Puede mostrar un borde alrededor de un widget de marco para separarlo visualmente de su entorno. Verá que esto se usa a menudo para hacer que una parte de la interfaz de usuario se vea hundida o elevada. Para hacer esto, debe establecer la borderwidth opción de configuración (que por defecto es 0, es decir, sin borde) y la relief opción que especifica la apariencia visual del borde.
Puede ser uno de los siguientes: 
    flat(predeterminado), 
    raised, 
    sunken, 
    solid, 
    ridge,
    groove.

    frame['borderwidth'] = 2
    frame['relief'] = 'sunken'
"""



"""
Changing Styles/Cambio de estilos

Los marcos tienen una style opción de configuración, que es común a todos los widgets temáticos. Esto le permite controlar muchos otros aspectos de su apariencia o comportamiento. Esto es un poco más avanzado, por lo que no entraremos en demasiados detalles ahora. Pero aquí hay un ejemplo rápido de cómo crear un marco de "Peligro" con un fondo rojo y un borde elevado.

    s = ttk.Style()
    s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
    ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()


    //Ejemplo para cambiar el estilo a todos los botones
    import ttk

    root.style = ttk.Style()
    #root.style.theme_use("clam")
    style.configure('TButton', background='black')
    style.configure('TButton', foreground='green')
    button= ttk.Button(self, text="My background is black and my foreground is green.")
"""