from CONEXION.LoginDao import listarLogin, guardarLogin

import tkinter as tk
from tkinter import messagebox, ttk, Toplevel, W
from PIL import Image, ImageTk

class Frame2(tk.Frame):
    """Clase ventana"""

    def __init__(self, login): 
        """Constructor de instancias"""
        super().__init__(login) 
        self.login = login
        self.pack(fill=tk.BOTH, expand=True)
        self.config(background="#0E4C75")
        self.widgets()
    
    def widgets(self):
        """Método que instancia todas las clases usadas de tkinter y poder colocarlas sobre el frame principal"""

        ########## Frame que contiene todo ################

        self.frame=tk.Frame(self)
        self.frame.configure(bg="#3282B5",width=770,height=500)
        self.frame.place(rely=0.18, relx=0.07)
        self.frame.pack_propagate(False)

        ######### Subdivisión 1 (Parte derecha) ###############

        self.frame1=tk.Frame(self.frame)
        self.frame1.configure(bg="#3282B5",width=450,height=500)
        self.frame1.pack(side=tk.RIGHT)
        self.frame1.pack_propagate(False)

        ######### Subdivisión 2 (Parte izquierda) ###############

        self.frame2=tk.Frame(self.frame)
        self.frame2.configure(bg="#2A6C96",width=320,height=500)
        self.frame2.pack(side=tk.LEFT)
        self.frame2.pack_propagate(False)
        
        ######### Subdivisión 1_1 (Parte derecha de subdivisión 1) ###############

        self.frame1_1=tk.Frame(self.frame1)
        self.frame1_1.configure(bg="#2A6C96",width=30,height=500)
        self.frame1_1.pack(side=tk.RIGHT)

        ######### Subdivisión 1_2 (Parte izquierda de subdivisión 1) #############

        self.frame1_2=tk.Frame(self.frame1)
        self.frame1_2.configure(bg="#3282B5",width=420,height=500)
        self.frame1_2.pack(side=tk.LEFT, padx=10)

        ######### Imagen de incógnito en subdivisión 2 #########

        self.imagenIncognito=Image.open("ICONOS/incognito.png")
        self.imagenIncognito=self.imagenIncognito.resize((280,250), Image.ANTIALIAS)
        self.imgIncognito=ImageTk.PhotoImage(self.imagenIncognito)
        self.LblImagenIncognito=tk.Label(self.frame2,image=self.imgIncognito)
        self.LblImagenIncognito.config(bg="#2A6C96")
        self.LblImagenIncognito.place(x=20,y=120) 
        
        self.LabelBienvenido=tk.Label(self.frame1_2)
        self.LabelBienvenido.configure(text="Bienvenido", font=("Bahnschrift", 50), bg="#3282B5", fg="#BDE2FF",anchor="c")
        self.LabelBienvenido.pack(pady=10)

        self.frame1_2_1=tk.Frame(self.frame1_2)
        self.frame1_2_1.configure(bg="#3282B5",width=420,height=500)
        self.frame1_2_1.pack()

        self.frame1_2_2=tk.Frame(self.frame1_2)
        self.frame1_2_2.configure(bg="#3282B5",width=420,height=500)
        self.frame1_2_2.pack()

        self.imagenUsername=Image.open("ICONOS/username.png")
        self.imagenUsername=self.imagenUsername.resize((70,70), Image.ANTIALIAS)
        self.imgUsername=ImageTk.PhotoImage(self.imagenUsername)
        self.LblImagenUsername=tk.Label(self.frame1_2_1,image=self.imgUsername)
        self.LblImagenUsername.config(bg="#2A6C96", width=50, height=45)
        self.LblImagenUsername.pack(side=tk.LEFT, pady=20) 
        self.LblImagenUsername.pack_propagate(False)

        self.svUsuario=tk.StringVar()
        self.EntryUsuario=tk.Entry(self.frame1_2_1)
        self.EntryUsuario.configure(bg="#FFFFFF", font=("Bahnschrift", 30), width=17, textvariable=self.svUsuario)
        self.EntryUsuario.pack(side=tk.RIGHT, pady=10)
        self.EntryUsuario.bind("<Button-1>",self.printb)

        self.imagenPassword=Image.open("ICONOS/password.png")
        self.imagenPassword=self.imagenPassword.resize((60,60), Image.ANTIALIAS)
        self.imgPassword=ImageTk.PhotoImage(self.imagenPassword)
        self.LblImagenPassword=tk.Label(self.frame1_2_2,image=self.imgPassword)
        self.LblImagenPassword.config(bg="#2A6C96", width=50, height=45)
        self.LblImagenPassword.pack(side=tk.LEFT, pady=20) 
        self.LblImagenPassword.pack_propagate(False)

        self.svContraseña=tk.StringVar()
        self.EntryContraseña=tk.Entry(self.frame1_2_2)
        self.EntryContraseña.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="*", width=17, textvariable=self.svContraseña)
        self.EntryContraseña.pack(side=tk.RIGHT, pady=20)

        self.frame1_2_3=tk.Frame(self.frame1_2)
        self.frame1_2_3.configure(bg="#3282B5")
        self.frame1_2_3.pack(fill=tk.BOTH, expand=True)

        self.svCheck=tk.BooleanVar()
        self.Check=tk.Checkbutton(self.frame1_2_3)
        self.Check.configure(text="Mostrar contraseña", font=("Bahnschrift",11),bg="#3282B5", activebackground="#3282B5", 
                            cursor="hand2",selectcolor="#2A6C96", variable=self.svCheck, command=self.mostrarContra)
        self.Check.pack(sid=tk.LEFT)

        self.frame1_2_4=tk.Frame(self.frame1_2)
        self.frame1_2_4.configure(bg="#3282B5",width=420,height=500)
        self.frame1_2_4.pack(padx=10, pady=10)

        self.Boton=tk.Button(self.frame1_2_4)
        self.Boton.configure(text="Login",font=("Bahnschrift", 20),bg="#BBE1F8",width=7, cursor="hand2", border=0, activebackground="#A3C5D9")
        self.Boton.pack(side=tk.LEFT)

        self.imagenLogin=Image.open("ICONOS/login.ico")
        self.imagenLogin=self.imagenLogin.resize((40,40), Image.ANTIALIAS)
        self.imgLogin=ImageTk.PhotoImage(self.imagenLogin)
        self.LblImagenLogin=tk.Label(self.frame1_2_4,image=self.imgLogin)
        self.LblImagenLogin.config(bg="#BBE1F8", width=50, height=50)
        self.LblImagenLogin.pack(side=tk.RIGHT) 
        self.LblImagenLogin.pack_propagate(False)

        self.Label2=tk.Label(self.frame1_2)
        self.Label2.configure(text="¿Olvidaste la contraseña?", font=("Bahnschrift", 10), bg="#3282B5", fg="#BDE2FF",anchor="c")
        self.Label2.pack(pady=10)
        self.Label2.bind("<Button-1>",self.Login)

        self.Label3=tk.Label(self.frame1_2)
        self.Label3.configure(text="¿No tienes cuenta? REGÍSTRATE", font=("Bahnschrift", 10), bg="#3282B5", fg="#BDE2FF",anchor="c")
        self.Label3.pack()

    def printb(self,event):
        messagebox.showinfo("USERNAME", "Ingresa el nombre del profesor de programación")

    def contrsa(self, event):
        pass

    def mostrarContra(self):
        """Método para mostrar * si el checkbutton está deshabilitado, si se habilita muestra el string ingresado"""

        if self.svCheck.get() == True:
            self.Entry2.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="", width=17, textvariable=self.svContraseña)
        else:
            self.Entry2.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="*", width=17, textvariable=self.svContraseña)

    def Corroborar(self):

        return True

    def TablaLogin(self):
        """Método que muestra todos los Trabajadores, sus usuarios y contraseñas en un Treeview"""

        try:

            self.ListaLogin = listarLogin()
            self.tablaLogin = ttk.Treeview(self.topLogin, column=("Trabajador", "Usuario", "Contraseña"))
            self.tablaLogin.config(height=10)
            self.tablaLogin.tag_configure("evenrow", background="oldlace")
            self.tablaLogin.grid(column=0, row=0, columnspan=3,sticky="nse")

            self.scroll=ttk.Scrollbar(self.topLogin, orient="vertical", command=self.tablaLogin.yview)
            self.scroll.grid(row=0, column=3, sticky="nse")

            self.tablaLogin.configure(yscrollcommand=self.scroll.set)

            self.tablaLogin.heading("#0",text="Trabajador")
            self.tablaLogin.heading("#1",text="Usuario")
            self.tablaLogin.heading("#2",text="Contraseña")

            self.tablaLogin.column("#0", anchor=W, width=200)
            self.tablaLogin.column("#1", anchor=W, width=60)
            self.tablaLogin.column("#2", anchor=W, width=60)


            for p in self.ListaLogin:
                self.tablaLogin.insert("",0,values=(p[0],p[1],p[2]), tags=("evenrow",))

        except:
            
            titulo = "Usuarios"
            mensaje = "Error al mostrar los usuarios"
            messagebox.showerror(titulo, mensaje)

    def Login(self, event):
        """Método para generar el Top Level donde estará la tabla de los historiales del paciente"""

        self.topLogin = Toplevel()
        self.topLogin.title("USUARIOS")
        self.topLogin.geometry("800x300+200+100")
        self.topLogin.resizable(width=False, height=False)
        self.topLogin.iconbitmap("ICONOS/incognito2.ico")
        self.topLogin.config(background="azure")
        
        self.TablaLogin() 


login = tk.Tk() 
login.title("LOGIN") 
login.resizable(width=True, height=True) 
login.geometry("900x760+350+20")
login.iconbitmap("ICONOS/login.ico")
fondo2 = Frame2(login)
fondo2.mainloop()