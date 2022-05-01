from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Label - Ejemplo 2 - imagenes")


mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(W, E, N, S))

image = PhotoImage(file='serpiente.gif')
label1 = ttk.Label(mainframe)
#label1 = ttk.Label(mainframe, image=image) // Así también se puede
label1.grid(column=0, row=0)
label1['image'] = image

root.mainloop()


"""
Visualización de imágenes

Las etiquetas también pueden mostrar una imagen en lugar de texto. Si solo desea que se muestre una imagen en su interfaz de usuario, esta es normalmente la forma de hacerlo. Veremos las imágenes con más detalle en un capítulo posterior, pero por ahora, supongamos que desea mostrar un GIF almacenado en un archivo en el disco. Este es un proceso de dos pasos. Primero, creará un "objeto" de imagen. Luego, puede decirle a la etiqueta que use ese objeto a través de su image opción de configuración:
"""


"""
Las etiquetas también pueden mostrar una imagen y texto al mismo tiempo. A menudo verá esto en los botones de la barra de herramientas. Para ello, utilice la compound opción de configuración. El valor predeterminado es none, lo que significa mostrar solo la imagen si está presente; si no hay imagen, muestra el texto especificado por las opciones texto . textvariable Otros valores posibles para la compound opción son text(solo texto), image(solo imagen), center(texto en el centro de la imagen), top(imagen sobre el texto), left, bottomy right.
"""


"""
Fuentes, colores y más

Al igual que con los marcos, normalmente no desea cambiar cosas como las fuentes y los colores directamente. Si necesita cambiarlos (por ejemplo, para crear un tipo especial de etiqueta), el método preferido sería crear un nuevo estilo, que luego usa el widget con la style opción.

A diferencia de la mayoría de los widgets temáticos, el widget de etiqueta también proporciona opciones de configuración explícitas específicas del widget como alternativa. Nuevamente, debe usarlos solo en casos especiales únicos cuando usar un estilo no necesariamente tiene sentido.

Puede especificar la fuente utilizada para mostrar el texto de la etiqueta utilizando la font opción de configuración. Si bien analizaremos las fuentes con más detalle en un capítulo posterior, estos son los nombres de algunas fuentes predefinidas que puede usar:

TkDefaultFont:          Predeterminado para todos los elementos de la GUI no especificados de otra manera.
TkTextFont:             Se utiliza para widgets de entrada, cuadros de lista, etc.
TkFixedFont:            Una fuente estándar de ancho fijo.
TkMenuFont:             La fuente utilizada para los elementos del menú.
TkHeadingFont:          Una fuente para encabezados de columna en listas y tablas.
TkCaptionFont:          Una fuente para las barras de subtítulos de ventanas y cuadros de diálogo.
TkSmallCaptionFont:     Títulos más pequeños para subventanas o cuadros de diálogo de herramientas.
TkIconFont:             Una fuente para leyendas de iconos.
TkTooltipFont:          Una fuente para información sobre herramientas.

        ejemplo:
            label['font'] = "TkDefaultFont"


El color de primer plano (texto) y de fondo de la etiqueta también se puede cambiar a través de las opciones de configuración foreground y background. Los colores se tratan en detalle más adelante, pero puede especificarlos como nombres de color (p. ej., red) o códigos RGB hexadecimales (p. ej., #ff340a).

Las etiquetas también aceptan la relief opción de configuración discutida para los marcos para que aparezcan hundidos o elevados.
"""



"""
Etiquetas multilínea

Las etiquetas pueden mostrar más de una línea de texto. Para hacerlo, inserte retornos de carro ( \n) en la cadena text(o ). textvariable. Las etiquetas también pueden envolver automáticamente su texto en varias líneas a través de la wraplength opción, que especifica la longitud máxima de una línea (en píxeles, centímetros, etc.).
"""