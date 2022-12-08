from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from io import open

ruta = ""  # Almacena la ruta del fichero


# funcion que pregunta si salir sin guardar
def CsinGuardar():
    mensaje.set("No te olvides de guardar")
    result = messagebox.askyesnocancel("Salir", "¿Quieres salir sin guardar?")
    if result is not None:  # None es Cancel esta condicional identifica a cancel para cancelar la operacion
        if result:
            root.destroy()
        else:
            guardar()
            root.destroy()
    else:
        pass


# funcion que compara el estado del fichero, contenido y ruta antes de guardar.
def sin_guardar(event=None):
    context = text.get(1.0, 'end-1c')  # Guarda el contenido del cuadro de texto
    if context != "":
        if ruta == "":
            CsinGuardar()

        else:
            fichero = open(ruta, 'r')  # Abre el fichero y guarda la informacion en la variable
            contenido = fichero.read()  # Lee el fichero y guarda el contenido
            if context != contenido:  # Compara las variables para detectar cambios en el fichero
                CsinGuardar()
            else:
                root.destroy()
    else:
        root.destroy()

# Funcion rehacer
def rehacer(event=None):
    text.edit_redo()
    mensaje.set("Rehecho")

# Funcion deshacer
def deshacer(event=None):
    text.edit_undo()
    mensaje.set("deshecho")

# funcion pegar
def pegar(event=None):
    text.insert(INSERT, root.clipboard_get())
    mensaje.set("Pegado")


# Funcion copiar
def copiar(event=None):
    mensaje.set("Copiado")
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())


# Funcion cortar
def cortar(event=None):
    mensaje.set("Cortado")
    root.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


# funcion selecionar to`do
def selecionar_todo(event=None):
    text.tag_add(SEL, "1.0", END)
    mensaje.set("Todo selecionado")


# Funcion eliminar
def eliminar(event=None):
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)
    mensaje.set("Eliminado")


# funcion nuevo fichero
def nuevo(event=None):  # event none permite ejecutar correctamente el metodo bind
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    text.delete(1.0, "end")
    root.title("Mi editor.")


# Funcion abrir fichero
def abrir(event=None):
    global ruta
    mensaje.set("Abrir fichero")
    ruta = filedialog.askopenfilename(initialdir="c:",
                                      filetypes=(("ficheros de texto", "*.txt"),),
                                      title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        text.insert('insert', contenido)
        fichero.close()
        root.title("Mi editor .  " + ruta)


# Funcion guardar fichero
def guardar(event=None):
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = text.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guadado!")
    else:
        guardar_como()


# Funcion guardar como
def guardar_como(event=None):
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = text.get(1.0, 'end-1c')
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

# Menu archivo
file_Menu = Menu(menubar, tearoff=0)
file_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=nuevo)
file_Menu.add_command(label="Abrir", accelerator="Ctrl+A", command=abrir)
file_Menu.add_command(label="Guardar", accelerator="Ctrl+G", command=guardar)
file_Menu.add_command(label="Guardar como", accelerator="Ctrl+G+Shift", command=guardar_como)
file_Menu.add_separator()  # Separador

file_Menu.add_command(label="Salir", accelerator="Ctrl+S", command=sin_guardar)
menubar.add_cascade(menu=file_Menu, label="Archivo")

# Menu editar.
edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=edit_menu, underline=0)

# Instrucciones de menu editar
edit_menu.add_command(label="Deshacer", compound='left', accelerator='Ctrl+Z', underline=0, command=deshacer)
edit_menu.add_command(label="Rehacer", compound='left', accelerator='Ctrl+Y', underline=0, command=rehacer)
edit_menu.add_separator()
edit_menu.add_command(label="Cortar", compound='left', accelerator='Ctrl+X', underline=0, command=cortar)
edit_menu.add_command(label="Copiar", compound='left', accelerator='Ctrl+C', underline=1, command=copiar)
edit_menu.add_command(label="Pegar", compound='left', accelerator='Ctrl+P', underline=0, command=pegar)
edit_menu.add_command(label="Eliminar", accelerator='Suprimir', underline=0, command=eliminar)
edit_menu.add_separator()
edit_menu.add_command(label="Selecionar todo", accelerator='Ctrl+E', underline=0, command=selecionar_todo)
edit_menu.add_command(label="Borrar todo", accelerator='Ctrl+L', underline=6)

# Menu formato
format_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Formato", menu=format_menu, underline=0)

# Instrucciones de menu formato
format_menu.add_command(label="Ajuste de linea")
format_menu.add_command(label="Fuente...")

# Caja de texto central
text = Text(root, undo=True)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side='left')

# Atajos del teclado
text.bind('<Control-n>', nuevo)
text.bind('<Control-a>', abrir)
text.bind('<Control-g>', guardar)
text.bind('<Control-Shift-S>', guardar_como)
text.bind('<Control-c>', copiar)
text.bind('<Control-x>', cortar)
text.bind('<Control-p>', pegar)
text.bind('<Delete>', eliminar)
text.bind('<Control-e>', selecionar_todo)
text.bind('<Control-s>', sin_guardar)
text.bind('<Control-z>', deshacer)
text.bind('<Control-y>', rehacer)

root.config(menu=menubar)
root.protocol('WM_DELETE_WINDOW', sin_guardar)

# Finalmente bucle de la aplicacion
root.mainloop()
