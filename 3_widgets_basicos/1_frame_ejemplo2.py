from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Agregar estilos a los frame")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style()
s.configure('mainframe.TFrame', 
                background="red",
                borderwidth=2,
                relief="sunken")

mainframe = ttk.Frame(root, width=500, height=500, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, E, S, N))

root.mainloop()