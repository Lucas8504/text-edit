from tkinter import *

#comfiguracion de la raiz
root = Tk()

# Variables dinamicas

texto = StringVar()
texto.set("un nuevo texto")

Label(root, text="hola mundo!").pack(anchor="nw")
label = Label(root, text="otra etiqueta")
label.pack(anchor="center")
Label(root, text="ultima etiqueta").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable = texto)

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack()

# finalmente bucle de la aplicacion
root.mainloop()