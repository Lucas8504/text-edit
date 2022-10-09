from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from io import open

ruta = ""  # Almacena la ruta del fichero

def salirSinGuardar():
    fichero = ""
    contenido = texto.get(1.0,'end-1c')
    if contenido != fichero:
        result = messagebox.askyesnocancel("Salir", "¿Quieres salir sin guardar?")
        if result != None:
            if result:
                root.destroy()
            else:
              guardar()
        else:
            pass
    else:
      root.destroy()



def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor.")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = filedialog.askopenfilename(initialdir="c:",
            filetypes =(("ficheros de texto", "*.txt"),),
            title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.insert('insert', contenido)
        fichero.close()
        root.title("Mi editor .  " + ruta)



def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guadado!")
    else:
        guardar_como()




def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guadado!")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Comfiguracion de la raiz
root = Tk()
root.title("Mi editor")


# Menu superior
menubar = Menu(root)
filemenu = Menu (menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
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
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
# Finalmente bucle de la aplicacion
root.protocol("WM_DELETE_WINDOW", salirSinGuardar)
root.mainloop()