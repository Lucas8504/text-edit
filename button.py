from tkinter import *


def sumar():
    r.set( float(n1.get()) + float(n2.get()))

def resta():
    r.set( float(n1.get()) - float(n2.get()))

def multi():
    r.set( float(n1.get()) * float(n2.get()))

def divi():
    r.set( float(n1.get()) / float(n2.get()))


# comfiguracion de la raiz
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Primer numero").pack()
Entry(root, justify="center", textvariable= n1).pack() # primer numero
Label(root, text="Segundo numero").pack()
Entry(root, justify="center", textvariable= n2).pack() # segundo numero
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable= r, state="disabled").pack() # resultado

Label(root, text=" ").pack()
Button(root,text="Suma", command= sumar).pack(side="left")
Button(root,text="Resta", command= resta).pack(side="left")
Button(root,text="Multiplica", command= multi).pack(side="left")
Button(root,text="Dividir", command= divi).pack(side="left")



# Finalmente bucle de la aplicacion
root.mainloop()