from tkinter import *

# comfiguracion de la raiz
root = Tk()


label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="w", padx=2, pady=2)   # row = fila, sticky es para alinear el label a un lado,
                                                          # padx y pady es para agregar una separacion

entry = Entry(root)
entry.grid(row=0, column=1, padx=2, pady=2)
entry.config(justify="right", state="normal")  # justify es para alinear entry y state es para habilitar o deshab.


label2 = Label(root, text="Apellido")
label2.grid(row=1, column=0, sticky="w", padx=2, pady=2)

entry2 = Entry(root)
entry2.grid(row=1, column=1, pady=2, padx=2)
entry2.config(justify="center", show="*") # show es para remplazar el contenido de entry por algun caracter especial.


# Finalmente bucle de la aplicacion
root.mainloop()