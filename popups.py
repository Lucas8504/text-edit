from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog


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
     # color = colorchooser.askcolor(title= "Elige un color")
     # print(color)
     # ruta = filedialog.askopenfilename(title="Abrir archivo", initialdir="c:", filetypes=(("Fichero de texto", "*.txt"), ("Archivo de textoHD", "*.txt2hd"), ("todos los ficheros", "*.*")))
     # print(ruta)

     # equivale a open (ruta, w) w predeterminado borra el archivo lo reemplazar otro
     fichero = filedialog.asksaveasfile(title="Guardar un archivo", mode="w", defaultextension=".txt")
     if fichero is not None:
         fichero.write("hola")
         fichero.close()



Button(root, text="Click", command=test).pack()



# Finalmente bucle de la aplicacion
root.mainloop()