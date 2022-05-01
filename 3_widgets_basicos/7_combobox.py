from tkinter import *
from tkinter import ttk

def  mostrar(*args):
    print(valor.get())
    print(combobox.current())

root = Tk()

valor = StringVar()
combobox = ttk.Combobox(root, textvariable=valor)
combobox.grid(column=0, row=0)

combobox['values'] = ('colombia', 'chile', 'venezuela')
combobox.bind("<<ComboboxSelected>>", mostrar) #Cuando el combobox este seleccionado activa la función mostrar
combobox.current(2)

root.mainloop()








"""
combobox

Un widget de cuadro combinado combina una entrada con una lista de opciones . Esto permite a los usuarios elegir entre un conjunto de valores que ha proporcionado (p. ej., configuraciones típicas), pero también poner su propio valor (p. ej., para casos menos comunes).


Los comboboxes se crean usando la ttk.Comboboxclase:
        countryvar = StringVar()
        country = ttk.Combobox(parent, textvariable=countryvar)



Al igual que las entradas, la textvariable opción vincula una variable en su programa al valor actual del cuadro combinado. Al igual que con otros widgets, debe inicializar la variable vinculada en su propio código.

Un cuadro combinado generará un <<ComboboxSelected>>evento virtual al que puede vincularse siempre que cambie su valor. (También puede realizar un seguimiento de los cambios en el textvariable, como hemos visto en los widgets anteriores que cubrimos. La vinculación al evento es más sencilla y, por lo tanto, tiende a ser nuestra opción preferida).

        country.bind('<<ComboboxSelected>>', function)
"""



"""
Valores predefinidos

Puede proporcionar una lista de valores que los usuarios pueden elegir mediante la valuesopción de configuración:

        country['values'] = ('USA', 'Canada', 'Australia')


También puede obtener el valor actual usando el get método y cambiar el valor actual usando el set método (que toma un solo argumento, el nuevo valor).

Para complementar los métodos get y set, también puede utilizar el current método para determinar qué elemento de la lista de valores predefinidos se selecciona. Llamada current sin argumentos; devolverá un índice basado en 0 en la lista o -1 si el valor actual no está en la lista. Puede seleccionar un elemento de la lista llamando current con un solo argumento de índice basado en 0.
"""