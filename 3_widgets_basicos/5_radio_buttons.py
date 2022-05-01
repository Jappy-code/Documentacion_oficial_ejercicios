from tkinter import *
from tkinter import ttk


def mostrar():
    try:
        if medida.get() == "300x200":
            root.geometry("300x200")
        
        elif medida.get() == "400x300":
            root.geometry("400x300")

        elif medida.get() == "500x400":
            root.geometry("500x400")

    except ValueError:
        pass

root = Tk()
root.title("Radio button")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(W, N, S, E))
mainframe['borderwidth'] = 2
mainframe['relief'] = 'sunken'

medida = StringVar()
peque=ttk.Radiobutton(mainframe, text='300x200', variable=medida, value='300x200', command= mostrar).grid(column=0, row=0)
medium=ttk.Radiobutton(mainframe, text='400x300', variable=medida, value='400x300', command= mostrar).grid(column=0, row=1)
maximo=ttk.Radiobutton(mainframe, text='500x400', variable=medida, value='500x400', command= mostrar).grid(column=0, row=2)

root.mainloop()


"""
Boton de radio

Un widget de botón de radio le permite elegir entre una de varias opciones mutuamente excluyentes. A diferencia de un botón de verificación, no están limitados a solo dos opciones. Los botones de radio siempre se usan juntos en un conjunto, donde varios widgets de botones de radio están vinculados a una sola opción o preferencia. Son apropiados para usar cuando el número de opciones es relativamente pequeño, por ejemplo, 3-5.
"""