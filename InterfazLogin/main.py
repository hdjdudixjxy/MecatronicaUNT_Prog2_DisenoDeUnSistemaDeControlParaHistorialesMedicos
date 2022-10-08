import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Login Usuario")

mainFrame = tk.Frame(root)
mainFrame.pack()

mainFrame.config(width=480, height=320)

titulo=tk.Label(mainFrame, text="Login de usuario con python", font=("Arial", 24))
titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

nombreLabel = tk.Label(mainFrame, text="Nombre: ")
nombreLabel.grid(column=0,row=1)
passLabel = tk.Label(mainFrame, text="Contraseña")
passLabel.grid(column=0,row=2)

nombreUsuario=tk.StringVar()
nombreEntry=tk.Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)

contraUsuario=tk.StringVar()
contraUsuario=tk.Entry(mainFrame, textvariable=contraUsuario, show="*")
contraUsuario.grid(column=1, row=2)

iniciarSesionButton =ttk.Button(mainFrame, text="Iniciar Sesion")
iniciarSesionButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

registrarSesionButton =ttk.Button(mainFrame, text="Registrar")
registrarSesionButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

root.mainloop()