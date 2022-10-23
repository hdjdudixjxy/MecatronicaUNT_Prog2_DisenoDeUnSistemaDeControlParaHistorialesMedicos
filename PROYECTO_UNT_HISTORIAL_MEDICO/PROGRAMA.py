import tkinter as tk
from tkinter import messagebox
from INTERFAZ.GUI import Frame, Frame2, error

def main():

    login = tk.Tk() 
    login.title("LOGIN") 
    login.resizable(width=True, height=True) 
    login.geometry("900x760+350+20")
    login.iconbitmap("ICONOS/login.ico")
    fondo2 = Frame2(login)
    fondo2.mainloop()

def recursivo():
    """Fución que nos ayudará a realizar una recursividad cuando el usuario quiera reintentar abrir la aplicación"""

    try:
        if __name__ == "__main__":
            
            main()

    except:
        error()

        resultado=messagebox.askretrycancel("ERROR", "Reintente abrir la aplicación")

        if resultado == True:
            
            recursivo() 

        elif resultado == False:
            print("Programa ejecutado sin éxito")

recursivo()

#### ATRIBUTOS-LEYENDA #######
# lbl"..." : significa Label
# sv "..." : es la variable de los entrys
# entry "..." : significa entry
# btn "..." : significa buttoncd