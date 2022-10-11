from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(True, True)
root.iconbitmap("png-transparent.ico")

frame = Frame(root, width=480, height=320)
frame.pack(fill="y", expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# abajo del tod0 para permitir la ejecucion de la ventana
root.mainloop()
# si cambiamos el nombre de la extencion .py por (.pyw) forzaremos a que no se habra la consola de fondo
