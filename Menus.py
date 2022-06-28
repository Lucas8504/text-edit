from tkinter import *

# comfiguracion de la raiz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)



menubar.add_cascade(label="Archivo", menu=filemenu)

filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="salir", command=root.quit)



editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editmenu)

editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")




# Finalmente bucle de la aplicacion
root.mainloop()