from tkinter import *
from tkinter import ttk

root = Tk()
l =Label(root, text="Starting...")
l.grid(column=0, row=0)
l.bind('<Enter>', lambda e: l.configure(text="Moved mouse inside"))
l.bind('<Leave>', lambda e: l.configure(text="Moved mouse outside"))
l.bind('<ButtonPress-1>', lambda e: l.configure(text="Clicked left mouse button"))
l.bind('<3>', lambda e: l.configure(text="Clicked right mouse button"))
l.bind('<Double-1>', lambda e: l.configure(text="Double clicked"))
l.bind('<B3-Motion>', lambda e: l.configure(text="right button drag to %d, %d" % (e.x, e.y)))

root.mainloop()

"""
Los dos primeros enlaces son bastante sencillos, solo buscan eventos simples. Un <Enter>evento significa que el mouse se ha movido sobre el widget, mientras que el <Leave>evento se genera cuando el mouse se mueve fuera del widget a otro diferente.
"""

"""
El siguiente enlace busca un clic del mouse, específicamente un <ButtonPress-1>evento. Aquí, el <ButtonPress>es el evento real, pero -1es un detalle del evento que especifica el botón izquierdo (principal) del mouse en el mouse. El enlace solo se activará cuando <ButtonPress>se genere un evento que involucre el botón principal del mouse. Si se hizo clic en otro botón del mouse, este enlace lo ignoraría.
"""

"""
Este siguiente enlace busca un <3>evento. Esto es en realidad una abreviatura de <ButtonPress-3>. Responderá a los eventos generados cuando se haga clic con el botón derecho del mouse.
"""

"""
 El siguiente enlace, <Double-1> (abreviatura de <Double-ButtonPress-1>) agrega otro modificador, Double y así responderá al hacer doble clic en el botón izquierdo del mouse.
"""

"""
El último enlace también usa un modificador: capturar el movimiento del mouse ( Motion), pero solo cuando B3se mantiene presionado el botón derecho del mouse ( ). Este enlace también muestra un ejemplo de cómo usar parámetros de eventos . Muchos eventos contienen información adicional, por ejemplo, la posición del mouse cuando se hace clic. Tk proporciona acceso a estos parámetros en los scripts de devolución de llamada de Tcl mediante el uso de sustituciones porcentuales . Estos porcentajes de sustituciones le permiten capturarlos para que puedan usarse en su script.

    Tkinter abstrae estas sustituciones porcentuales y en su lugar encapsula todos los parámetros del evento en un objeto de evento. Arriba, usamos los campos x and y para recuperar la posición del mouse. Veremos las sustituciones porcentuales que se usan más adelante en otro contexto, la validación del widget de entrada.
"""

    #¿Qué pasa con las lambdaexpresiones? Tkinter espera que proporcione una función como devolución de llamada del evento, cuyo primer argumento es un objeto de evento que representa el evento que activó la devolución de llamada. A veces no vale la pena molestarse en definir funciones regulares con nombre para devoluciones de llamada triviales únicas, como en este ejemplo. En su lugar, acabamos de usar las funciones anónimas de Python a través de lambda. En aplicaciones reales, casi siempre usará una función regular, como la calculatefunción en nuestro ejemplo de pies a metros, o un método de un objeto.

"""
Acabamos de ver cómo se pueden configurar enlaces de eventos para un widget individual. Cuando ese widget recibe un evento coincidente, el enlace se activará. Pero eso no es todo lo que puedes hacer.

Su enlace puede capturar no solo un solo evento, sino también una breve secuencia de eventos. El <Double-1>enlace se activa cuando se producen dos clics del mouse en poco tiempo. Puede hacer lo mismo para capturar dos teclas presionadas seguidas, por ejemplo, <KeyPress-A><KeyPress-B>o simplemente <ab>.
"""

"""
A continuación se describen los eventos más utilizados, junto con las circunstancias en las que se generan. Algunos se generan en unas plataformas y en otras no. Para obtener una descripción completa de todos los diferentes nombres de eventos, modificadores y los diferentes parámetros de eventos que están disponibles con cada uno, el mejor lugar para buscar es la bindreferencia de comandos.

<Activate>:         La ventana se ha vuelto activa.
<Deactivate>:       La ventana ha sido desactivada.
<MouseWheel>:       Se ha movido la rueda de desplazamiento del ratón.
<KeyPress>:         Se ha presionado la tecla del teclado.
<KeyRelease>:       La clave ha sido liberada.
<ButtonPress>:      Se ha pulsado un botón del ratón.
<ButtonRelease>:    Se ha soltado un botón del ratón.
<Motion>:           El ratón se ha movido.
<Configure>:        El widget ha cambiado de tamaño o posición.
<Destroy>:          El widget está siendo destruido.
<FocusIn>:          Al widget se le ha dado el enfoque del teclado.
<FocusOut>:         El widget ha perdido el foco del teclado.
<Enter>:            El puntero del mouse ingresa al widget.
<Leave>:            El puntero del mouse deja el widget.
"""

"""
El detalle del evento para los eventos del mouse es el botón que se presionó, por ejemplo, 1, 2o 3. Para eventos de teclado, es la tecla específica, por ejemplo, A, 9, space, plus, comma, equal. Puede encontrar una lista completa en la keysymsreferencia de comandos.

Los modificadores de eventos pueden incluir, por ejemplo, B1o Button1para indicar que se mantiene presionado el botón principal del mouse, Doubleo Triplepara secuencias del mismo evento. Modificadores de teclas para cuando las teclas del teclado se mantienen presionadas en línea Control, Shift, Alt, Optiony Command.
"""