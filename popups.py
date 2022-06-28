from tkinter import *
from tkinter import messagebox


# Configuracion de la raiz
root = Tk()

def test():
     # messagebox.showinfo("hola", "Hola mundo")
     # messagebox.showwarning("Alerta", "Solo administrador")
     # messagebox.showerror("Huu...", "Borraste Sistem32")
     # resultado = messagebox.askquestion("Salir","¿Estas seguro que deseas salir sin guardar?")
     # if resultado == "yes":
     #   root.destroy()
     # resultado = messagebox.askokcancel("Salir", "¿Estas seguro que deseas salir sin guardar?")
     # if resultado:
     #   root.destroy()



Button(root, text="Click", command=test).pack()


# Finalmente bucle de la aplicacion
root.mainloop()