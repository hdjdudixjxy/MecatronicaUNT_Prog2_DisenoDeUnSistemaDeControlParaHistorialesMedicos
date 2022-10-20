import tkinter as tk
from tkinter import messagebox
from INTERFAZ.GUI import Frame, error

def main():
    """Interfaz principal"""

    aplicacion = tk.Tk() 
    aplicacion.title("HISTORIAS CLINICAS") # nombre de la interfaz
    aplicacion.resizable(width=False, height=False) # expansión a pantalla completa
    aplicacion.geometry("1420x720+48+40") # tamaño por defecto y posición
    aplicacion.minsize(width=1280, height=720) # tamaño mínimo al minimizar
    aplicacion.iconbitmap("ICONOS/ICONO.ico") # icono de la interfaz
    fondo = Frame(aplicacion) # ventana para dar color de fondo
    fondo.mainloop() # bucle generador

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
# btn "..." : significa button