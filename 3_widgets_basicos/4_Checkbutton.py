from tkinter import *
from tkinter import ttk

def aceptar_terminos():
    if validacion.get() == 'no':
        button_siguiente.state(['disabled'])
    
    elif validacion.get() == 'si':
        button_siguiente.state(['!disabled'])

root = Tk()
root.title("Checkbutton")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(W, E, S, N))

label_titulo = ttk.Label(mainframe, text="Términos y condiciones").grid(column=0, row=0)

label_contenido = ttk.Label(mainframe, text="¿Aceptas los términos y condiciones?").grid(column=0, row=1)

validacion = StringVar()
check = ttk.Checkbutton(mainframe, text="Aceptar los terminos y condiciones",
                        command=aceptar_terminos, variable=validacion,
                        onvalue='si', offvalue='no')
check.grid(column=0, row=2)

button_siguiente = ttk.Button(mainframe, text="NEXT")
button_siguiente.grid(column=0, row=3)
button_siguiente.state(['disabled'])

root.mainloop()


"""
Botón de verificación/Checkbutton

Un widget de botón de verificación es como un botón normal que también contiene un valor binario de algún tipo (es decir, un conmutador). Cuando se presiona, un botón de verificación activa la palanca y luego invoca su devolución de llamada. Los widgets de botón de verificación se utilizan con frecuencia para permitir que los usuarios activen o desactiven una opción.


Los botones de verificación se crean utilizando la ttk.Checkbuttonclase. Por lo general, sus contenidos y comportamiento se especifican al mismo tiempo:

        measureSystem = StringVar()
        check = ttk.Checkbutton(parent, text='Use Metric', 
                                command=metricChanged, variable=measureSystem,
                                onvalue='metric', offvalue='imperial')
"""