from tkinter import *

# Comfiguracion de la raiz
root = Tk()


texto = Text(root)                      # Text abre un cuadro de texto
texto.pack()
texto.config(width=30, height=15)       # funciona con caracteres y
                                        # no con pixeles (30 x 15 caracteres)
texto.config(font="Consolas", padx=15, pady=15)
texto.config(selectbackground="red")     # color de fondo de seleccion


# Finalmente bucle de alplicacion
root.mainloop()