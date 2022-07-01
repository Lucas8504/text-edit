from tkinter import *
from tkinter import filedialog
from io import open

ruta = "" # Almacena la ruta del fichero

def Nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor.")


def Abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = filedialog.askopenfilename(initialdir="C:",
            filetypes=(("ficheros de texto", "*.txt"),),
            title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.insert('insert', contenido)
        fichero.close()
        root.title("Mi editor.  " + ruta)



def Guardar():
    mensaje.set("Guardar fichero")



def Guardar_como():
    mensaje.set("Guardar fichero como")




# Comfiguracion de la raiz
root = Tk()
root.title("Mi editor")


# Menu superior
menubar = Menu(root)
filemenu = Menu (menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=Nuevo)
filemenu.add_command(label="Abrir", command=Abrir)
filemenu.add_command(label="Guardar", command=Guardar)
filemenu.add_command(label="Guardar como", command=Guardar_como)
filemenu.add_separator()

filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

#Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor imferior
mensaje = StringVar()
mensaje.set("Biemvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
# Finalmente bucle de la aplicacion
root.mainloop()
