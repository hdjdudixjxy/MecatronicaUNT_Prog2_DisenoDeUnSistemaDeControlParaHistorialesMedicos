# Página: https://hdjdudixjxy.github.io./
from ast import Pass
from Conexion.PacienteDao import DatosPaciente, editarDatoPaciente, guardarDatoPaciente, listar, listarCondicion, eliminarPaciente
from Conexion.HistorialDao import guardarHistoria, editarHistoria, eliminarHistoria, listarHistoria
from Conexion.OperacionesDao import guardarOperaciones, eliminarOperaciones, listarPrecio, listarOperacion
from Conexion.LoginDao import listarLogin, guardarLogin, listarCondicionLogin, listarCondicionLogin2

import tkinter as tk
from tkinter import W, Menu, ttk, messagebox, Toplevel

import tkcalendar as tc
import datetime
from PIL import Image, ImageTk
import fpdf

from email import message
import smtpd, ssl
import smtplib
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tkinter import filedialog as FileDialog
import subprocess
import webbrowser
import mouse

################## VENTANA DE FONDO ##########################

class Frame(tk.Frame):
    """Clase ventana"""

    def __init__(self, aplicacion): 
        """Constructor de instancias"""

        super().__init__(aplicacion) # utilizamos super() para llevar a cabo herencias múltiples, de las subclases a la superclase
        self.aplicacion = aplicacion
        self.pack(fill=tk.BOTH, expand=True)
        self.config(background="#777067", relief=tk.GROOVE, border=5)
        self.aplicacion.bind("<Escape>",self.eventoSalir)
        self.aplicacion.bind("<Control-l>",self.eventoLight)
        self.aplicacion.bind("<Control-d>",self.eventoDark)

        self.barra_menus=tk.Menu(self.aplicacion)
        
        self.claroimg=Image.open("ICONOS/claro.png")
        self.claroimg=self.claroimg.resize((30,30), Image.ANTIALIAS)

        self.oscuroimg=Image.open("ICONOS/oscuro.png")
        self.oscuroimg=self.oscuroimg.resize((30,30), Image.ANTIALIAS)

        self.claroimgen=ImageTk.PhotoImage(self.claroimg)
        self.oscuroimgen=ImageTk.PhotoImage(self.oscuroimg)

        self.menu_archivo = tk.Menu(self.barra_menus, tearoff=False) 
        
        self.variable=tk.IntVar()
        self.variable.set(2)
        self.menu_archivo.add_radiobutton(variable=self.variable, value=1, label="Claro", accelerator="Ctrl+L", image=self.claroimgen, 
                                            compound=tk.LEFT, command=self.tema, font=("verdana",10))
        self.menu_archivo.add_radiobutton(variable=self.variable, value=2,label="Oscuro", accelerator="Ctrl+D", image=self.oscuroimgen,
                                            compound=tk.LEFT, command=self.tema, font=("verdana",10))
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", accelerator="ESC", command=self.aplicacion.destroy)
        self.menu_archivo.configure(bg="#B2B4AC", activebackground="#D1D2CD", activeforeground="black")

        self.barra_menus.add_cascade(menu=self.menu_archivo, label="Temas")
        
        self.aplicacion.configure(menu=self.barra_menus)

        self.idPersona = None
        self.idPersonaHistoria=None
        self.idHistoriaMedica=None
        self.idHistoriaMedicaEditar=None
        self.camposPaciente()
        self.tablaPaciente()
        self.deshabilitar()
        
    def tema(self):
        """Método que cambia los colores de los widgets"""

        if self.variable.get() == 1: # claro
            
            self.imagen=Image.open("ICONOS/medico2.png")
            self.imagen=self.imagen.resize((200,190), Image.ANTIALIAS)
            self.img=ImageTk.PhotoImage(self.imagen)
            self.LblImagen=tk.Label(self,image=self.img)
            self.LblImagen.config(bg="#B2B4AC")
            self.LblImagen.grid(column=4,row=2,rowspan=5, columnspan=2)

            ############## CAMBIOS DE COLOR ##################

            self.config(background="#B2B4AC", relief=tk.GROOVE, border=5)

            self.listaCambioslbl_claro=[self.lblNombre,self.lblApellidos,self.lblDni,self.lblFechNacimiento, self.lblEdad, self.lblTelefono, self.lblCorreo, self.lblBuscarDni]

            for i in self.listaCambioslbl_claro:
                i.configure(font=("verdana",15,"bold"), bg="#B2B4AC", anchor = "w",fg="#777067")

            self.listaCambiosentry_claro=[self.entryNombre,self.entryApellidos,self.entryDni,self.entryFecNacimiento, self.entryEdad, self.entryTelefono, self.entryCorreo, self.entryBuscarDni]

            for i in self.listaCambiosentry_claro:
                i.configure(font=("verdana",15), bg="#D1D2CD", selectbackground="#777067", selectforeground="white")

            self.listaCambiosbutton_claro=[self.btnNuevo,self.btnGuardar,self.btnCancelar,self.btnCalendario, self.btnBuscarCondicion,self.btnEditarPaciente
                                        ,self.btnEliminarPaciente, self.btnHistorialPaciente]

            for i in self.listaCambiosbutton_claro:
                i.configure(font=("verdana",12,"bold"), bg="#777067", cursor="hand2",activebackground="#867E74")

            
            self.tabla.tag_configure("evenrow", background="#777067")

        elif self.variable.get() == 2: # oscuro

            self.imagen=Image.open("ICONOS/medico1.png")
            self.imagen=self.imagen.resize((200,190), Image.ANTIALIAS)
            self.img=ImageTk.PhotoImage(self.imagen)
            self.LblImagen=tk.Label(self,image=self.img)
            self.LblImagen.config(bg="#777067")
            self.LblImagen.grid(column=4,row=2,rowspan=5, columnspan=2)

            ############## CAMBIOS DE COLOR ##################

            self.config(background="#777067", relief=tk.GROOVE, border=5)

            self.listaCambioslbl_oscuro=[self.lblNombre,self.lblApellidos,self.lblDni,self.lblFechNacimiento, self.lblEdad, self.lblTelefono, self.lblCorreo, self.lblBuscarDni]

            for i in self.listaCambioslbl_oscuro:
                i.configure(font=("verdana",15,"bold"), bg="#777067", anchor = "w",fg="#D1D2CD")

            self.listaCambiosentry_oscuro=[self.entryNombre,self.entryApellidos,self.entryDni,self.entryFecNacimiento, self.entryEdad, self.entryTelefono, self.entryCorreo, self.entryBuscarDni]

            for i in self.listaCambiosentry_oscuro:
                i.configure(font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")

            self.listaCambiosbutton_oscuro=[self.btnNuevo,self.btnGuardar,self.btnCancelar,self.btnCalendario, self.btnBuscarCondicion, self.btnEditarPaciente
                                        ,self.btnEliminarPaciente, self.btnHistorialPaciente]

            for i in self.listaCambiosbutton_oscuro:
                i.configure(font=("verdana",12,"bold"), bg="#B2B4AC", cursor="hand2",activebackground="#D1D2CD")

            self.tabla.tag_configure("evenrow", background="#D1D2CD")

    def eventoSalir(self,event):
        """Evento que se ejecuta al presionar ESC en la pantalla principal"""

        self.aplicacion.destroy()

    def eventoLight(self, event):
        """Evento que se ejecuta al presionar CTRL+L en la pantalla principal"""

        self.variable.set(1)
        self.tema()

    def eventoDark(self,event):
        """Evento que se ejecuta al presionar CTRL+D en la pantalla principal"""

        self.variable.set(2)
        self.tema()

################## WIDGETS DE LA VENTANA PRINCIPAL ######################

    def camposPaciente(self):
        """Método que instancia todas las clases usadas de tkinter y poder colocarlas sobre el frame principal"""
        
        ##################### LABELS ##########################

        self.lblNombre = tk.Label(self, text="NOMBRE COMPLETO: ")
        self.lblNombre.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblNombre.grid(column=0, row=0, pady=5)

        self.lblApellidos = tk.Label(self, text="APELLIDOS COMPLETOS: ")
        self.lblApellidos.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblApellidos.grid(column=0,row=1, pady=5)

        self.lblDni = tk.Label(self, text="DNI: ")
        self.lblDni.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblDni.grid(column=0,row=2, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text="FECHA DE NACIMIENTO: ")
        self.lblFechNacimiento.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblFechNacimiento.grid(column=0,row=3, pady=5)

        self.lblEdad = tk.Label(self, text="EDAD: ")
        self.lblEdad.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblEdad.grid(column=0,row=4, pady=5)

        self.lblTelefono = tk.Label(self, text="TELÉFONO: ")
        self.lblTelefono.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblTelefono.grid(column=0,row=5, pady=5) 

        self.lblCorreo = tk.Label(self, text="CORREO ELECTRÓNICO: ")
        self.lblCorreo.config(font=("verdana",15,"bold"), background="#777067", anchor = "w",fg="#D1D2CD")
        self.lblCorreo.grid(column=0,row=6, pady=5)

        ######################### ENTRYS ###############################

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellidos = tk.StringVar()
        self.entryApellidos = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApellidos.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryFecNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryCorreo.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        ######################### BUTTONS ####################################

        self.btnNuevo = tk.Button(self, text="NUEVO", command=self.habilitar)
        self.btnNuevo.config(width=20, font=("verdana",12,"bold"), 
                                background="#B2B4AC", cursor="hand2",activebackground="#D1D2CD")
        self.btnNuevo.grid(column=0,row=7, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text="GUARDAR", command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=("verdana",12,"bold"), 
                                background="#B2B4AC", cursor="hand2",activebackground="#D1D2CD")
        self.btnGuardar.grid(column=1,row=7, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text="CANCELAR")
        self.btnCancelar.config(width=20, font=("verdana",12,"bold"), 
                                background="#B2B4AC", cursor="hand2",activebackground="#D1D2CD", command=self.deshabilitar)
        self.btnCancelar.grid(column=2,row=7, padx=10, pady=5)

        self.btnCalendario = tk.Button(self, text="BUSCAR")
        self.btnCalendario.config(width=13, font=("verdana",12,"bold"), command=self.MostrarCalendario,
                                background="#B2B4AC", cursor="hand2",activebackground="#D1D2CD")
        self.btnCalendario.grid(column=3,row=3,padx=10,pady=5)

        #################### WDGETS DEL BUSCADOR ########################
        
        self.lblBuscarDni = tk.Label(self, text="Buscar DNI: ")
        self.lblBuscarDni.config(font=("verdana",15,"bold"), bg="#777067",fg="#D1D2CD")
        self.lblBuscarDni.grid(column=3, row=0, padx=2, pady=5)

        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=("verdana",15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryBuscarDni.grid(column=4, row=0, padx=2, pady=5)

        self.btnBuscarCondicion = tk.Button(self, text="BUSCAR", command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=10, font=("verdana",12,"bold"), 
                                bg="#B2B4AC", cursor="hand2",activebackground="#D1D2CD")
        self.btnBuscarCondicion.grid(column=4,row=1, padx=2, pady=5)

        ################### IMAGEN ########################

        self.imagen=Image.open("ICONOS/medico1.png")
        self.imagen=self.imagen.resize((200,190), Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(self.imagen)
        self.LblImagen=tk.Label(self,image=self.img)
        self.LblImagen.config(bg="#777067")
        self.LblImagen.grid(column=4,row=2,rowspan=5, columnspan=2)

################ FUNCIONES PARA LA VENTANA PRINCIPAL  ###################
            
    def deshabilitar(self):
        """Método que bloquea los entrys, para después habilitarlos con el botón NUEVO"""

        self.idPersona = None
        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svFecNacimiento.set("")
        self.svEdad.set("")
        self.svTelefono.set("")
        self.svCorreo.set("")

        self.entryNombre.config(state="disabled")
        self.entryApellidos.config(state="disabled")
        self.entryDni.config(state="disabled")
        self.entryFecNacimiento.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.entryCorreo.config(state="disabled")
        self.entryTelefono.config(state="disabled")

        self.btnCancelar.config(state="disabled")
        self.btnGuardar.config(state="disabled")
    
    def habilitar(self):
        """Método para habilitar los entrys"""

        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svTelefono.set("")
        self.svCorreo.set("")

        self.entryNombre.config(state="normal")
        self.entryApellidos.config(state="normal")
        self.entryDni.config(state="normal")
        self.entryFecNacimiento.config(state="normal")
        self.entryEdad.config(state="normal")
        self.entryCorreo.config(state="normal")
        self.entryTelefono.config(state="normal")

        self.btnCancelar.config(state="normal")
        self.btnGuardar.config(state="normal")        

    def buscarCondicion(self):
        """Método para el entry buscar por DNI"""

        if len(self.svBuscarDni.get()) > 0:
            where = "WHERE 1=1" # manda todos los valores de la base de datos
            if len(self.svBuscarDni.get()) > 0:
                where = "WHERE Dni = " + self.svBuscarDni.get() + "" 
                self.tablaPaciente(where) # muestra en la interfaz los datos de la persona con el dni ingresado
            else:
                self.tablaPaciente() # si no se encuentra ese where dni entonces no se mostrará nada
        else:
            if len(self.svBuscarDni.get()) == 0: # si no colocamos nada en el entry de buscar dni, nos mostrará todos los inactivos
                where = "WHERE activo = 0 "
                self.tablaPaciente(where)

    def tablaPaciente(self, where = ""):
        """Método que inserta la tabla treeView de ttk en la GUI de tkinter"""

        if len(where) > 0:
            self.listaDatosPaciente = listarCondicion(where)
        else:
            self.listaDatosPaciente = listar()
            self.listaDatosPaciente.reverse()

        self.tabla = ttk.Treeview(self, column=("NombreCompleto", "ApellidosCompletos","DNI","FechaNacimiento","Edad","NumeroTelefonico","CorreoElectronico")) 
        #ttk.Treeview crea la tabla 
        self.tabla.grid(column=0, row=8, columnspan=5, sticky="nswe")
        
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=8, column=4, sticky="nse")
        self.tabla.config(height=15)

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure("evenrow", background="#D1D2CD") # damos color a las filas

        #definimos los títulos de cada columna

        self.tabla.heading("#0",text="ID")
        self.tabla.heading("#1",text="Nombres")
        self.tabla.heading("#2",text="Apellidos")
        self.tabla.heading("#3",text="DNI")
        self.tabla.heading("#4",text="F. Nacimiento")
        self.tabla.heading("#5",text="Edad")
        self.tabla.heading("#6",text="Telefono")
        self.tabla.heading("#7",text="Correo")

        self.tabla.column("#0", anchor=W, width=1)
        self.tabla.column("#1", anchor=W, width=120)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=20)
        self.tabla.column("#4", anchor=W, width=100)
        self.tabla.column("#5", anchor=W, width=3)
        self.tabla.column("#6", anchor=W, width=40)
        self.tabla.column("#7", anchor=W, width=120)

        for p in self.listaDatosPaciente:
            self.tabla.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7]), tags=("evenrow",)) # con tags referenciamos el tag configure que hicimos anteriormente

        # Creamos los nuevos botones debajo de la tabla

        self.btnEditarPaciente = tk.Button(self, text="Editar Paciente", command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=("verdana",12,"bold"), bg="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnEditarPaciente.grid(row=9, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text="Eliminar Paciente", command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=("verdana",12,"bold"), bg="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnEliminarPaciente.grid(row=9, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text="Historial Paciente", command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=50,font=("verdana",12,"bold"), bg="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnHistorialPaciente.grid(row=9, column=2, columnspan=3, pady=5)

################# FUNCIONES DEL CALENDARIO ###################

    def MostrarCalendario(self):
        """Método que muestra el calendario en la interfaz"""

        self.topCalendario = Toplevel() #Creamos una ventana flotante
        self.topCalendario.title("FECHA DE NACIMIENTO")
        self.topCalendario.geometry("300x300+1000+80")
        self.topCalendario.resizable(width=False, height=False)
        self.topCalendario.iconbitmap("ICONOS/calendario.ico")
        
        self.calendar = tc.Calendar(self.topCalendario, selectmode="day", year=1990, month=3, day=20,locale ="es_US", 
                                    background="burlywood4", foreground="gray2", bordercolor="burlywood3", headersbackground="burlywood3",
                                    headersforeground="gray2",selectbackground="burlywood2", selectforeground="gray2",normalbackground="burlywood1",
                                    normalforeground="gray2",weekendbackground="burlywood1",weekendforeground="gray2", othermonthbackground="wheat3", 
                                    othermonthforeground="gray2", othermonthwebackground="wheat3", othermonthweforeground="gray2", cursor = "hand2", 
                                    date_pattern="dd/mm/Y")
        self.calendar.pack(fill=tk.BOTH, expand=True)

        self.btnCalendario2 = tk.Button(self.topCalendario, text="INSERTAR")
        self.btnCalendario2.config(width=13, font=("verdana",12,"bold"), command=self.EnviarFecha,
                                background="navajowhite3", cursor="hand2",activebackground="navajowhite4")
        self.btnCalendario2.pack(fill=tk.BOTH)

    def EnviarFecha(self):
        """Método que envía la fecha de self.calendar al entry FecNacimiento y referencia a la función calcularEdad"""

        self.svFecNacimiento.set(self.calendar.get_date()) # Mediante set mandamos la fecha al entry y con get_date la obtenemos de self.calendar 

        if len(self.calendar.get_date())>1: # Condición para referenciar la función CalcularEdad
            self.CalcularEdad()
            self.topCalendario.destroy() 

    def CalcularEdad(self): 
        """Método que inserta la edad en el entry Edad, restando el año obtenido con el modulo datetime y el ingresado por self.calendar"""

        self.fechaActual = datetime.date.today()
        self.date1 = self.calendar.get_date()
        self.convertidor = datetime.datetime.strptime(self.date1, "%d/%m/%Y") # Retorna datetime correspondiente a self.date1, analizado según format
        # Se usa strptime, porque necesitamos que sea compatible con el módulo datetime, ya que fue generado por tkcalendar

        self.resultado = self.fechaActual.year - self.convertidor.year
        self.svEdad.set(self.resultado)

############## FUNCIONES QUE VINCULAN LOS OBJETOS #############

    def guardarPaciente(self):
        """Método para insertar los datos del paciente a la base de datos"""

        persona = DatosPaciente(self.svNombre.get(), self.svApellidos.get(), self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(),self.svTelefono.get(), self.svCorreo.get())
        # el metodo get lee lo que se inserta en los entrys

        if self.idPersona == None: # si el id no tiene valor, entonces guarda el dato, sino solo lo vamos a editar
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        self.deshabilitar() # una vez presionado el boton duardar, se va a borrar todos los datos de los entrys
        self.tablaPaciente() # para actualizar la tabla cuando se ingresan datos
    
    def editarPaciente(self):
        """Método que cambia los datos, pero en la tabla de la GUI"""

        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"] #Trae el ID
            self.NombrePaciente = self.tabla.item(self.tabla.selection())["values"][0] # agrega los datos de el objeto ya insertado a uno nuevo, para poder editarlo
            self.ApellidosPaciente = self.tabla.item(self.tabla.selection())["values"][1]
            self.DNIPaciente = self.tabla.item(self.tabla.selection())["values"][2]
            self.FecNacimientoPaciente = self.tabla.item(self.tabla.selection())["values"][3]
            self.EdadPaciente = self.tabla.item(self.tabla.selection())["values"][4]
            self.TelefonoPaciente = self.tabla.item(self.tabla.selection())["values"][5]
            self.CorreoPaciente = self.tabla.item(self.tabla.selection())["values"][6]

            self.habilitar()

            # el cero va por que el método insert lleva la siguiente forma insert(parent, index, ...) y parent es el identificador del elemento para crear un nuevo elemento
            
            self.entryNombre.insert(0, self.NombrePaciente) # con el metodo insert, hacemos que aparezcan los datos ya puestos en la tabla, en cada entry
            self.entryApellidos.insert(0, self.ApellidosPaciente)
            self.entryDni.insert(0, self.DNIPaciente)
            self.entryFecNacimiento.insert(0, self.FecNacimientoPaciente)
            self.entryEdad.insert(0, self.EdadPaciente)
            self.entryTelefono.insert(0, self.TelefonoPaciente)
            self.entryCorreo.insert(0, self.CorreoPaciente)
            
        except:
            title = "Editar Paciente"
            mensaje = "Error al editar paciente"
            messagebox.showerror(title, mensaje)  

    def eliminarDatoPaciente(self):
        """Método que elimina los pacientes de la tabla y no de la base de datos"""

        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"]
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
            
        except:
            title = "Eliminar Paciente"
            mensaje = "No se pudo eliminar paciente"
            messagebox.showinfo(title, mensaje)  

################ TOP LEVEL HISTORIA MÉDICA ################

    def tablaHistoria(self):
        """Método que muestra todos los historiales del paciente en un Treeview"""
        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())["text"]
                self.idPersonaHistoria = self.idPersona

            if self.idPersona > 0:

                idPersona = self.idPersona

            self.ListaHistoria = listarHistoria(idPersona)
            self.tabla2 = ttk.Treeview(self.topHistoriaMedica, column=("Paciente", "FechaHistoria", "MotivoDeLaVisita", "Operacion", "Tratamiento", "DetalleAdicional", "Precio"))
            self.tabla2.config(height=10)
            self.tabla2.tag_configure("evenrow", background="#D1D2CD")
            self.tabla2.grid(column=0, row=0, columnspan=8,sticky="nse")

            self.scroll2=ttk.Scrollbar(self.topHistoriaMedica, orient="vertical", command=self.tabla2.yview)
            self.scroll2.grid(row=0, column=8, sticky="nse")

            self.tabla2.configure(yscrollcommand=self.scroll2.set)

            self.tabla2.heading("#0",text="ID")
            self.tabla2.heading("#1",text="Paciente")
            self.tabla2.heading("#2",text="Fecha y Hora")
            self.tabla2.heading("#3",text="Motivo de la visita")
            self.tabla2.heading("#4",text="Operacion")
            self.tabla2.heading("#5",text="Tratamiento")
            self.tabla2.heading("#6",text="Detalle adicional")
            self.tabla2.heading("#7",text="Precio")

            self.tabla2.column("#0", anchor=W, width=40)
            self.tabla2.column("#1", anchor=W, width=200)
            self.tabla2.column("#2", anchor=W, width=150)
            self.tabla2.column("#3", anchor=W, width=200)
            self.tabla2.column("#4", anchor=W, width=150)
            self.tabla2.column("#5", anchor=W, width=270)
            self.tabla2.column("#6", anchor=W, width=420)
            self.tabla2.column("#7", anchor=W, width=65)

            for p in self.ListaHistoria:
                self.tabla2.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7]), tags=("evenrow",))

        except:
            
            titulo = "Historia Medica"
            mensaje = "Error al mostrar historial"
            messagebox.showerror(titulo, mensaje)
            self.idPersona = None

    def historiaMedica(self):
        """Método para generar el Top Level donde estará la tabla de los historiales del paciente"""

        self.topHistoriaMedica = Toplevel()
        self.topHistoriaMedica.title("HISTORIAL MEDICO")
        self.topHistoriaMedica.geometry("1515x280+5+10")
        self.topHistoriaMedica.resizable(width=False, height=False)
        self.topHistoriaMedica.iconbitmap("ICONOS/Historial.ico")
        self.topHistoriaMedica.config(background="#777067")
        
        self.tablaHistoria() 

        self.btnGuardarHistoria=tk.Button(self.topHistoriaMedica, text="Agregar Historia", command=self.topAgregarHistoria)
        self.btnGuardarHistoria.config(width=18, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnGuardarHistoria.grid(column=0, row=1, padx=10, pady=10)

        self.btnEditarHistoria=tk.Button(self.topHistoriaMedica, text="Editar Historia",command=self.topEditarHistorialMedico)
        self.btnEditarHistoria.config(width=18, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnEditarHistoria.grid(column=1, row=1, padx=10, pady=10)

        self.btnEliminarHistoria=tk.Button(self.topHistoriaMedica, text="Eliminar Historia", command=self.eliminarHistorialMedico)
        self.btnEliminarHistoria.config(width=18, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnEliminarHistoria.grid(column=2, row=1, padx=10, pady=10)

        self.btnPDF=tk.Button(self.topHistoriaMedica, text="Generar PDF",command=self.crearPDF)
        self.btnPDF.config(width=18,font=("Verdana", 12, "bold"), foreground="gray2",
                                    background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnPDF.grid(column=3, row=1,padx=10,pady=10)

        self.btnEnviarEmail=tk.Button(self.topHistoriaMedica, text="Enviar Historial",command=self.enviarEmail)
        self.btnEnviarEmail.config(width=18,font=("Verdana", 12, "bold"), foreground="gray2",
                                    background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnEnviarEmail.grid(column=4, row=1,padx=10,pady=10)

        self.btnVerPDF=tk.Button(self.topHistoriaMedica, text="Ver Historial",command=self.verPDF)
        self.btnVerPDF.config(width=18,font=("Verdana", 12, "bold"), foreground="gray2",
                                    background="#B2B4AC", activebackground="#D1D2CD", cursor="hand2")
        self.btnVerPDF.grid(column=5, row=1,padx=10,pady=10)

        self.idPersona = None
        
    def crearPDF(self):
        """Método para crear el historial de cada paciente"""
        
        self.pdf=fpdf.FPDF(orientation="L",unit="mm",format="A4")
        self.pdf.add_page()
        
        self.id=self.tabla2.item(self.tabla2.selection())["text"]
        self.n=self.tabla2.item(self.tabla2.selection())["values"][0]
        self.f=self.tabla2.item(self.tabla2.selection())["values"][1]
        self.a=self.tabla2.item(self.tabla2.selection())["values"][2]
        self.b=self.tabla2.item(self.tabla2.selection())["values"][3]
        self.c=self.tabla2.item(self.tabla2.selection())["values"][4]
        self.d=self.tabla2.item(self.tabla2.selection())["values"][5]
        self.g=str(self.tabla.item(self.tabla.selection())["values"][2])
        self.pe=self.tabla2.item(self.tabla2.selection())["values"][6]

        self.pdf.set_font("Arial","",14)
        self.pdf.text(x=230,y=10, txt = "Generado el: "+ str(datetime.date.today()))
        self.pdf.text(x=130, y=200, txt = "Trujillo-PERÚ")

        self.pdf.image("ICONOS/medico.png", x=245, y=20, w=45, h=45)
        self.pdf.image("ICONOS/vigo.png", x=45, y=138, w=40, h=20)
        self.pdf.image("ICONOS/jonathan.png", x=130, y=138, w=40, h=20)
        self.pdf.image("ICONOS/victor.png", x=215, y=138, w=40, h=20)
        self.pdf.image("ICONOS/elias.png", x=175, y=163, w=40, h=20)
        self.pdf.image("ICONOS/luis.png", x=87, y=163, w=40, h=20)

        self.pdf.set_font("Arial","B",20) 
        self.pdf.text(x=100, y=15, txt="CLÍNICA SÁNCHEZ JIMENEZ")

        self.pdf.set_font("Arial","B",16)
        self.pdf.text(x=10, y=35, txt="Paciente:")
        self.pdf.text(x=10, y=48, txt="DNI:")
        self.pdf.text(x=10, y=61, txt="Motivo de la visita a la clínica:")
        self.pdf.text(x=10, y=74, txt="Fecha y hora de la visita:")
        self.pdf.text(x=10, y=87, txt="Su operación fue: ")
        self.pdf.text(x=10, y=101, txt="Monto a pagar: ")
        self.pdf.text(x=10, y=114, txt="Debe seguir el siguiente tratamiento:")
        self.pdf.text(x=10, y=127, txt="Detalles adicionales:")

        self.pdf.set_font("Arial","",16)
        self.pdf.text(x=40, y=35, txt=self.n)
        self.pdf.text(x=30, y=48, txt=self.g)
        self.pdf.text(x=100, y=61, txt=self.a)
        self.pdf.text(x=90, y=74, txt=self.f)
        self.pdf.text(x=70, y=87, txt=f"{self.b}")
        self.pdf.text(x=65, y=101, txt=f"{self.pe} soles")
        self.pdf.text(x=120, y=114, txt=self.c)
        self.pdf.text(x=80, y=127, txt=self.d)

        self.pdf.set_font("Arial","B",14)
        self.pdf.text(x=35,y=158, txt="Vigo Villar Cristhian A.")
        self.pdf.text(x=117,y=158, txt="Sanchez Rojas Jonathan A.") 
        self.pdf.text(x=200,y=158, txt="Valdiviezo Jimenez Victor J.")
        self.pdf.text(x=82,y=183, txt="Valdez Julca Luis A.") 
        self.pdf.text(x=165,y=183, txt="Ortiz Salvador Edinson E.")

        self.pdf.set_font("Arial","",14)
        self.pdf.text(x=50, y=163, txt="Cirujano")
        self.pdf.text(x=137, y=163, txt="Practicante")
        self.pdf.text(x=220, y=163, txt="Traumatólogo")
        self.pdf.text(x=97, y=188, txt="Conserje")
        self.pdf.text(x=185, y=188, txt="Electricista")

        self.pdf.output(f"HISTORIALES_PDF/Historial_{self.id}_{self.n}.pdf")
      
    def verPDF(self):
        """Método para visualizar un historial"""

        resultado=messagebox.askquestion("HISTORIALES.PDF", "¿Deseas ver toda la carpeta de historiales?")

        if resultado == "yes":

            self.fichero = FileDialog.askopenfilename(title="Abrir un historial") # Guarda la ruta que seleccionemos en el atributo fichero 
            subprocess.Popen([self.fichero], shell=True) # Abre el fichero seleccionado

        elif resultado == "no":

            self.id2=self.tabla2.item(self.tabla2.selection())["text"]
            self.n2=self.tabla2.item(self.tabla2.selection())["values"][0]

            subprocess.Popen([f"HISTORIALES_PDF/Historial_{self.id2}_{self.n2}.pdf"], shell=True) # Abre el fichero seleccionado

    def enviarEmail(self):
        """Método para enviar los historiales a correos hotmail"""

        pass
        """        servidor = "smtp.gmail.com"
                                    puerto = 465
                                    remitente = "t1513600121@unitru.edu.pe"
                                    password = "74855615"
                                    ab=self.tabla.item(self.tabla2.selection())["values"][6]
                                    receptor = str(ab)
                                    contexto = ssl.create_default_context()
                                    titulo = "ENVÍO DE HISTORIAL MÉDICO"
                                    no=self.tabla.item(self.tabla2.selection())["values"][0]
                                    cuerpo = f"Hola {no}
                                    Reciba los más cordiales saludos de parte del Centro Médico especializado Sánchez Jimenez.
                                    El motivo de este mensaje es para comunicarle que le hacemos llegar su ficha médica correspondiente al día de hoy.
                                    
                                    Me despido, no sin antes recordarle que me encuentro a su disposición y, ante cualquier consulta adicional, comuníquese al 
                                    WhatsApp +51 955 216 891 o al correo electrónico registros@gmail.com. 
                                    Recalco nuestro compromiso asumido para contribuir en el desarrollo de su salud.
                                    Sin otro particular, le reitero nuestros cordiales saludos.
                                    Muy atentamente,

                                    Asistente de Coordinación
                                    Centro Médico especializado Sánchez Jimenez  
                                    "

                                    message = MIMEMultipart()
                                    message["subject"] = titulo
                                    message["From"] = remitente
                                    message["To"] = receptor

                                    message.attach(MIMEText(cuerpo, "plain"))
                                    self.id2=self.tabla2.item(self.tabla2.selection())["text"]
                                    self.nombre2=self.tabla2.item(self.tabla2.selection())["values"][0]
                                    archivo = f"D:\\CRISTHIAN\\universidad\\ciclo 4\\Programación II\\MecatronicaUNT_Prog2_DisenoDeUnSistemaDeControlParaHistorialesMedicos\\PROYECTO_UNT_HISTORIAL_MEDICO\\HISTORIALES_PDF\\Historial_{self.id2}_{self.nombre2}.pdf"

                                    with open(archivo, "rb") as adjunto:
                                        part = MIMEBase("Aplication", "octet-stream")
                                        part.set_payload(adjunto.read())

                                    encoders.encode_base64(part)
                                    part.add_header("Content-Disposition", f"attachment; filename={archivo}",)

                                    message.attach(part)
                                    texto = message.as_string()

                                    with smtplib.SMTP_SSL(servidor, puerto, context=contexto) as s:
                                        s.login(remitente, password)
                                        s.sendmail(remitente, receptor, texto)"""

    def TopLevelOperaciones(self):
        """Método que genera el list box con las operaciones"""

        self.root=tk.Toplevel()

        self.root.title("OPERACIONES MÉDICAS")
        self.root.geometry("480x790+1030+15") 
        self.root.resizable(0,0)
        self.root.iconbitmap("ICONOS/icon.ico")
        self.root.configure(background="#777067") 

        ################ CLASES FRAME ###############

        self.ventana1=tk.Frame(self.root)
        self.ventana1.configure(bg="#777067",height=150)

        self.ventana2=tk.LabelFrame(self.root)
        self.ventana2.configure(text="Eliga la operación", font=("Verdana", 15, "bold"), border=5, bg="#777067")

        self.subventana1=tk.Frame(self.ventana2, bg="#777067")
        self.subventana2=tk.Frame(self.ventana2, bg="#777067")

        ########## CLASES ENTRYS ################

        self.operacion=tk.StringVar()
        
        self.entry=tk.Entry(self.ventana1)
        self.entry.configure(textvariable=self.operacion, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")

        self.precio=tk.IntVar()

        self.entry2=tk.Entry(self.ventana1)
        self.entry2.configure(textvariable=self.precio, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")

        ########## CLASES LABELS ############

        self.etiqueta1=tk.Label(self.ventana1)
        self.etiqueta1.configure(text="Operación a agregar", font=("Verdana", 15, "underline", "bold"),bg="#777067")

        self.etiqueta2=tk.Label(self.ventana1)
        self.etiqueta2.configure(text="Monto a pagar", font=("Verdana", 15, "underline", "bold"),bg="#777067")

        ################ CLASE LISTBOX #####################

        self.lista=tk.Listbox(self.subventana1)
        self.lista.configure(bg="#D1D2CD", selectbackground="#B2B4AC", selectforeground="black", width=28, height=15,
                        font=("Verdana", 15), cursor="hand2", justify=tk.LEFT, selectborderwidth=4)

        self.ListaOperacion=listarOperacion() # Ejecutamos la funcion listarOperación para generar la lista y poder insertar los *args en el LISTBOX
        self.ListaOperacionTRUE=[]            # Creamos esta lista vacía que será con la que trabajaremos ya que no queremos una lista con *args
                                              # tuples, sino str
        
        for p in range(len(self.ListaOperacion)): # Aquí hacemos varias listas por que la lista que se retorna es una lista que contiene elementos como
                                                  # tuplas y queremos elementos como string para que no surga error al mostrarlos en el listbox, ni
                                                  # en los entrys de historial medico
            self.ListaOperacion2=self.ListaOperacion[p]
            self.lista.insert(tk.END,self.ListaOperacion2[0])
            self.ListaOperacionTRUE.append(self.ListaOperacion2[0])
        
        self.ListaPrecio=listarPrecio()
        self.ListaPrecioTRUE=[]

        for p in range(len(self.ListaPrecio)): # Aquí hacemos varias listas por que la lista que se retorna es una lista que contiene elementos como
                                                  # tuplas y queremos elementos como string para que no surga error al mostrarlos en el listbox, ni
                                                  # en los entrys de historial medico
            self.ListaPrecio2=self.ListaPrecio[p]
            self.ListaPrecioTRUE.append(self.ListaPrecio2[0])

        def agregar_datos():
            """Función para agregar las operaciones y el precio tanto a la lista como a el list box y a la base de datos"""

            Operacion=self.operacion.get()
            Precio=self.precio.get()
            
            try:
                if Operacion in self.ListaOperacionTRUE:
                    
                    titulo = "Agregar operación"
                    mensaje = "Esta operación ya se encuentra en la base de datos"
                    messagebox.showinfo(titulo, mensaje)
                    self.topAHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    self.root.destroy()
                    self.historiaMedica()
                    self.topAgregarHistoria()   # No es necesario colocar el self.TopLevelOperaciones() ya que en este método ya referenciamos esa función
                
                elif Operacion==None:
                    titulo = "Agregar operación"
                    mensaje = "Inserte un valor para la operación"
                    messagebox.showinfo(titulo, mensaje)
                    self.topAHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    self.root.destroy()
                    self.historiaMedica()
                    self.topAgregarHistoria()
                    
                elif isinstance(Precio,int):

                    self.ListaOperacionTRUE.append(Operacion)
                    ultimaOperacion=self.ListaOperacionTRUE[-1]
                    self.lista.insert(tk.END,ultimaOperacion) 

                    self.ListaPrecioTRUE.append(Precio)
                    ultimoPrecio=self.ListaPrecioTRUE[-1]
                    guardarOperaciones(ultimaOperacion, ultimoPrecio)

                    self.topAHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    
                    self.historiaMedica()
                    self.topAgregarHistoria()
                    

                else:
                    pass         

            except:
                
                titulo = "Agregar operación"
                mensaje = "Error al agregar operación"
                messagebox.showerror(titulo, mensaje)
                self.topAHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topAgregarHistoria()
                
        def eliminar_datos():
            """Función para eliminar datos tanto de la lista como del list box y de la base de datos"""

            tupla=(self.lista.curselection())
            numeroParaLista=(tupla[0])

            try:
                self.lista.delete(numeroParaLista)              # Lo borramos del ListBox
                self.ListaOperacionTRUE.pop(numeroParaLista)    # Lo eliminamos de la lista
                self.ListaPrecio.pop(numeroParaLista) 
                eliminarOperaciones(numeroParaLista+1)          # Sumamos 1 porque SQL toma valores del ID desde 1 y python desde 0 y para borrar el 
                                                                # elemento correcto, sumamos 1
                
                self.topAHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topAgregarHistoria()

            except:

                titulo = "Eliminar operación"
                mensaje = "Error al eliminar la operación"
                messagebox.showerror(titulo, mensaje)
                self.topAHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topAgregarHistoria()
                
        def insertar_datos():
            """Función para insertar las operaciones y el precio en el TopLevel"""

            tupla=(self.lista.curselection())
            numeroParaLista=(tupla[0])

            try:
                self.root.destroy()
                self.topAHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.historiaMedica()
                self.topAgregarHistoria()
                self.root.destroy()                 # Damos doble destroy porque este se ejecuta cuando se ejecuta el método topAgregarHistoria
                self.svOperacion.set(str(self.ListaOperacionTRUE[numeroParaLista]))
                self.svPrecio.set(int(self.ListaPrecioTRUE[numeroParaLista]))

            except IndexError:
                
                titulo = "Insertar operación"
                mensaje = "Error al insertar la operación"
                messagebox.showerror(titulo, mensaje)
                self.topAHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.historiaMedica()
                self.topAgregarHistoria()

        ########## CLASES BUTTON #############
        
        self.boton1=tk.Button(self.ventana1)
        self.boton1.configure(text="AGREGAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="#D1D2CD", command=agregar_datos)

        self.boton2=tk.Button(self.ventana1)
        self.boton2.configure(text="ELIMINAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="#D1D2CD", command=eliminar_datos)

        self.boton3=tk.Button(self.root)
        self.boton3.configure(text="INSERTAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 13, "bold"), activebackground="#D1D2CD", width=28, command=insertar_datos)

        self.scrollbar1 = tk.Scrollbar(self.subventana2) 
        self.scrollbar1.configure(orient="vertical", command = self.lista.yview) 
        self.lista.configure(yscrollcommand = self.scrollbar1.set) 
        
        self.scrollbar2 = tk.Scrollbar(self.subventana1)
        self.scrollbar2.configure(orient="horizontal", command = self.lista.xview) 

        self.lista.config(xscrollcommand = self.scrollbar2.set) 
        
        self.ventana1.pack(fill=tk.X)
        self.ventana2.pack(padx=10,pady=10)
        self.entry.place(x=40,y=36)
        self.entry2.place(x=40,y=104)
        self.boton1.place(x=325,y=34)
        self.boton2.place(x=325,y=102)
        self.etiqueta1.place(x=40,y=0)
        self.etiqueta2.place(x=40,y=66)
        self.boton3.pack(pady=6)
        self.subventana1.pack(side = tk.LEFT, fill = tk.BOTH)
        self.subventana2.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.lista.pack()
        self.scrollbar1.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.scrollbar2.pack(side = tk.BOTTOM, fill = tk.BOTH)
        
    def TopLevelOperacionesEditar(self):
        """Método que genera el list box con las operaciones, pero para editar"""

        self.root=tk.Toplevel()

        self.root.title("OPERACIONES MÉDICAS")
        self.root.geometry("480x790+1030+15") 
        self.root.resizable(0,0)
        self.root.iconbitmap("ICONOS/icon.ico")
        self.root.configure(background="#777067") 

        ################ CLASES FRAME ###############

        self.ventana1=tk.Frame(self.root)
        self.ventana1.configure(bg="#777067",height=150)

        self.ventana2=tk.LabelFrame(self.root)
        self.ventana2.configure(text="Eliga la operación", font=("Verdana", 15, "bold"), border=5, bg="#777067")

        self.subventana1=tk.Frame(self.ventana2, bg="#777067")
        self.subventana2=tk.Frame(self.ventana2, bg="#777067")

        ########## CLASES ENTRYS ################

        self.operacion=tk.StringVar()
        
        self.entry=tk.Entry(self.ventana1)
        self.entry.configure(textvariable=self.operacion, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")

        self.precio=tk.IntVar()

        self.entry2=tk.Entry(self.ventana1)
        self.entry2.configure(textvariable=self.precio, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")

        ########## CLASES LABELS ############

        self.etiqueta1=tk.Label(self.ventana1)
        self.etiqueta1.configure(text="Operación a agregar", font=("Verdana", 15, "underline", "bold"),bg="#777067")

        self.etiqueta2=tk.Label(self.ventana1)
        self.etiqueta2.configure(text="Monto a pagar", font=("Verdana", 15, "underline", "bold"),bg="#777067")

        ################ CLASE LISTBOX #####################

        self.lista=tk.Listbox(self.subventana1)
        self.lista.configure(bg="#D1D2CD", selectbackground="#B2B4AC", selectforeground="black", width=28, height=15,
                        font=("Verdana", 15), cursor="hand2", justify=tk.LEFT, selectborderwidth=4)

        self.ListaOperacion=listarOperacion()
        self.ListaOperacionTRUE=[]            
        
        for p in range(len(self.ListaOperacion)): 
                                                  
            self.ListaOperacion2=self.ListaOperacion[p]
            self.lista.insert(tk.END,self.ListaOperacion2[0])
            self.ListaOperacionTRUE.append(self.ListaOperacion2[0])
        
        self.ListaPrecio=listarPrecio()
        self.ListaPrecioTRUE=[]

        for p in range(len(self.ListaPrecio)): 
                                                  
            self.ListaPrecio2=self.ListaPrecio[p]
            self.ListaPrecioTRUE.append(self.ListaPrecio2[0])

        def agregar_datos_editar():
            """Función para agregar las operaciones y el precio tanto al diccionario como a el list box"""

            Operacion=self.operacion.get()
            Precio=self.precio.get()
            
            try:
                if Operacion in self.ListaOperacionTRUE:
                    
                    titulo = "Agregar operación"
                    mensaje = "Esta operación ya se encuentra en la base de datos"
                    messagebox.showinfo(titulo, mensaje)
                    self.topEditarHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    self.root.destroy()
                    self.historiaMedica()
                    self.topEditarHistorialMedico()  
                
                elif Operacion==None:
                    titulo = "Agregar operación"
                    mensaje = "Inserte un valor para la operación"
                    messagebox.showinfo(titulo, mensaje)
                    self.topEditarHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    self.root.destroy()
                    self.historiaMedica()
                    self.topEditarHistorialMedico()
                    
                elif isinstance(Precio,int):

                    self.ListaOperacionTRUE.append(Operacion)
                    ultimaOperacion=self.ListaOperacionTRUE[-1]
                    self.lista.insert(tk.END,ultimaOperacion) 

                    self.ListaPrecioTRUE.append(Precio)
                    ultimoPrecio=self.ListaPrecioTRUE[-1]
                    guardarOperaciones(ultimaOperacion, ultimoPrecio)

                    self.topEditarHistoria.destroy()
                    self.topHistoriaMedica.destroy()
                    
                    self.historiaMedica()
                    self.topEditarHistorialMedico()
                    
                else:
                    pass         

            except:

                titulo = "Agregar operación"
                mensaje = "Error al agregar operación"
                messagebox.showerror(titulo, mensaje)
                self.topEditarHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topEditarHistorialMedico()
                
        def eliminar_datos_editar():
            """Función para eliminar datos del diccionario operaciones"""

            tupla=(self.lista.curselection())
            numeroParaLista=(tupla[0])

            try:

                self.lista.delete(numeroParaLista)              
                self.ListaOperacionTRUE.pop(numeroParaLista)    
                self.ListaPrecio.pop(numeroParaLista) 
                eliminarOperaciones(numeroParaLista+1)          

                self.topEditarHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topEditarHistorialMedico()
                
            except:

                titulo = "Eliminar operación"
                mensaje = "Error al eliminar la operación"
                messagebox.showerror(titulo, mensaje)
                self.topEditarHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.root.destroy()
                self.historiaMedica()
                self.topEditarHistorialMedico()
                
        def insertar_datos_editar():
            """Función para insertar las operaciones y el precio, pero esta vez en el top level editar historial paciente"""

            tupla=(self.lista.curselection())
            numeroParaLista=(tupla[0])

            try:
             
                self.svOperacionEditar.set(str(self.ListaOperacionTRUE[numeroParaLista]))
                self.svPrecioEditar.set(int(self.ListaPrecioTRUE[numeroParaLista]))
                self.root.destroy() 

            except IndexError:
                
                titulo = "Insertar operación"
                mensaje = "Error al insertar la operación"
                messagebox.showerror(titulo, mensaje)
                self.topEditarHistoria.destroy()
                self.topHistoriaMedica.destroy()
                self.historiaMedica()
                self.topEditarHistorialMedico()

        ########## CLASES BUTTON #############
        
        self.boton1=tk.Button(self.ventana1)
        self.boton1.configure(text="AGREGAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="#D1D2CD", command=agregar_datos_editar)

        self.boton2=tk.Button(self.ventana1)
        self.boton2.configure(text="ELIMINAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 12, "bold"), activebackground="#D1D2CD", command=eliminar_datos_editar)

        self.boton3=tk.Button(self.root)
        self.boton3.configure(text="INSERTAR", bg="#B2B4AC", cursor="hand2", font=("Verdana", 13, "bold"), activebackground="#D1D2CD", width=28, command=insertar_datos_editar)

        self.scrollbar1 = tk.Scrollbar(self.subventana2) 
        self.scrollbar1.configure(orient="vertical", command = self.lista.yview) 
        self.lista.configure(yscrollcommand = self.scrollbar1.set) 
        
        self.scrollbar2 = tk.Scrollbar(self.subventana1)
        self.scrollbar2.configure(orient="horizontal", command = self.lista.xview) 

        self.lista.config(xscrollcommand = self.scrollbar2.set) 
        
        self.ventana1.pack(fill=tk.X)
        self.ventana2.pack(padx=10,pady=10)
        self.entry.place(x=40,y=36)
        self.entry2.place(x=40,y=104)
        self.boton1.place(x=325,y=34)
        self.boton2.place(x=325,y=102)
        self.etiqueta1.place(x=40,y=0)
        self.etiqueta2.place(x=40,y=66)
        self.boton3.pack(pady=6)
        self.subventana1.pack(side = tk.LEFT, fill = tk.BOTH)
        self.subventana2.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.lista.pack()
        self.scrollbar1.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.scrollbar2.pack(side = tk.BOTTOM, fill = tk.BOTH)

    def topAgregarHistoria(self):
        """Método para generar el Top Level donde agregaremos los datos del historial"""

        self.TopLevelOperaciones()

        self.topAHistoria = tk.Toplevel()
        self.topAHistoria.title("AGREGAR HISTORIA")
        self.topAHistoria.geometry("900x530+100+300")
        self.topAHistoria.resizable(width=False, height=False)
        self.topAHistoria.iconbitmap("ICONOS/ICONO.ico")
        self.topAHistoria.config(background="#777067")

        ##################### FRAME 1 ##########################

        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(background="#777067")
        self.frameDatosHistoria.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)

            ##################### LABELS-F1 ##########################

        self.lblMotivo = tk.Label(self.frameDatosHistoria, text="Motivo de la visita", width=30, font=("Verdana", 15,"bold"), background="#777067")
        self.lblMotivo.grid(row=0, column=0, padx=5, pady=3)

        self.lblOperacion = tk.Label(self.frameDatosHistoria, text="Operación", width=20, font=("Verdana", 15,"bold"), background="#777067")
        self.lblOperacion.grid(row=2, column=0, padx=5, pady=3)
        
        self.lblTratamiento = tk.Label(self.frameDatosHistoria, text="Tratamiento", width=20, font=("Verdana", 15,"bold"), background="#777067")
        self.lblTratamiento.grid(row=4, column=0, padx=5, pady=3)

        self.lblDetalle = tk.Label(self.frameDatosHistoria, text="Detalle adicional", width=30, font=("Verdana", 15,"bold"), background="#777067")
        self.lblDetalle.grid(row=6, column=0, padx=5, pady=3)

        self.lblPrecio = tk.Label(self.frameDatosHistoria, text="Precio", width=20, font=("Verdana", 15,"bold"), background="#777067")
        self.lblPrecio.grid(row=8, column=0, padx=5, pady=3)

            ##################### ENTRYS-F1 ##########################

        self.svMotivo = tk.StringVar()
        self.Motivo = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivo)
        self.Motivo.config(width=64, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.Motivo.grid(row=1, column=0, padx= 5, pady=3, columnspan=2)

        self.svOperacion = tk.StringVar()
        self.Operacion = tk.Entry(self.frameDatosHistoria, textvariable=self.svOperacion)
        self.Operacion.config(width=64, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.Operacion.grid(row=3, column=0, padx= 5, pady=3, columnspan=2)

        self.svTratamiento = tk.StringVar()
        self.Tratamiento = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamiento)
        self.Tratamiento.config(width=64, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.Tratamiento.grid(row=5, column=0, padx= 5, pady=3, columnspan=2)

        self.svDetalle = tk.StringVar()
        self.Detalle = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalle)
        self.Detalle.config(width=64, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.Detalle.grid(row=7, column=0, padx= 5, pady=3, columnspan=2)

        self.svPrecio = tk.IntVar()
        self.Precio = tk.Entry(self.frameDatosHistoria, textvariable=self.svPrecio)
        self.Precio.config(width=64, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.Precio.grid(row=9, column=0, padx= 5, pady=3, columnspan=2)

        ##################### FRAME 2 ##########################

        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg="#777067")
        self.frameFechaHistoria.pack(fill=tk.BOTH, expand=True, padx=20,pady=10)

            ##################### LABELS-F2 ##########################

        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text="Fecha y Hora", width=20, font=("Verdana", 15,"bold"), background="#777067")
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        
            ##################### ENTRYS-F2 ##########################

        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        
            ##################### FECHA Y HORA-F2 ####################

        xFecha=str(datetime.date.today().strftime("%d/%m/%Y, "))
        xHora=str(datetime.datetime.now().strftime("%I:%M %p"))
        self.svFechaHistoria.set(xFecha+xHora) 

            ##################### BUTTONS-F2 ##########################

        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Agregar", command=self.agregaHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=("Verdana", 12,"bold"), background="#B2B4AC", cursor="hand2", activebackground="#D1D2CD")
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Salir",command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=("Verdana", 12,"bold"), background="#B2B4AC", cursor="hand2", activebackground="#D1D2CD")
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

        self.idPersona = None

    def agregaHistorialMedico(self):
        """Método que agrega los historiales"""

        try:
            if self.idHistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(),self.svMotivo.get(), self.svOperacion.get(), self.svTratamiento.get(),self.svDetalle.get(),self.svPrecio.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.root.destroy()
            
            self.historiaMedica()
            self.idPersona = None

        except:
            titulo = "Agregar Historia"
            mensaje = "Error al agregar historia Medica"
            messagebox.showerror(titulo, mensaje)

    def eliminarHistorialMedico(self):
        """Método que elimina los historiales, de forma definitiva"""

        try:
            self.idHistoriaMedica = self.tabla2.item(self.tabla2.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)
            self.topHistoriaMedica.destroy()
            self.historiaMedica()
            self.idHistoriaMedica = None
            
        except:
            titulo = "Eliminar Historia"
            mensaje = "Error al eliminar"
            messagebox.showerror(titulo, mensaje)

    def topEditarHistorialMedico(self):
        """Método para generar el Top Level donde editaremos los datos del historial """
        try:

            self.TopLevelOperacionesEditar()

            self.idHistoriaMedica = self.tabla2.item(self.tabla2.selection())["text"]
            self.fechaHistoriaEditar = str(datetime.date.today().strftime("%d/%m/%Y, ") + datetime.datetime.now().strftime("%I:%M %p"))
            self.motivoHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][2]
            self.operacionHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][3]
            self.tratamientoHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][4]
            self.detalleHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][5]
            self.precioEditar = self.tabla2.item(self.tabla2.selection())["values"][6]

            self.topEditarHistoria = tk.Toplevel()
            self.topEditarHistoria.geometry("910x510+100+310")
            self.topEditarHistoria.title("EDITAR HISTORIA MEDICA")
            self.topEditarHistoria.resizable(width=False, height=False)
            self.topEditarHistoria.iconbitmap("ICONOS/ICONO.ico")
            self.topEditarHistoria.config(background="#777067")

            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(background="#777067")
            self.frameEditarHistoria.pack(fill=tk.BOTH, expand=True, padx=20,pady=10)

            #LABEL EDITAR HISTORIA

            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text="Motivo de la visita", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=3)

            self.lblOperacionEditar = tk.Label(self.frameEditarHistoria, text="Operación", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblOperacionEditar.grid(row=2, column=0, padx=5, pady=3)

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text="Tratamiento", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblTratamientoEditar.grid(row=4, column=0, padx=5, pady=3)

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text="Detalle adicional", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblDetalleEditar.grid(row=6, column=0, padx=5, pady=3)

            self.lblPrecioeEditar = tk.Label(self.frameEditarHistoria, text="Precio", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblPrecioeEditar.grid(row=8, column=0, padx=5, pady=3)

            #ENTRYS EDITAR HISTORIA

            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
            self.entryMotivoEditar.grid(row = 1, column=0, pady=3, padx=5, columnspan=2)

            self.svOperacionEditar = tk.StringVar()
            self.entryOperacionEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svOperacionEditar)
            self.entryOperacionEditar.config(width=65, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
            self.entryOperacionEditar.grid(row = 3, column=0, pady=3, padx=5, columnspan=2)

            self.svTratamientoEditar = tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=65, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
            self.entryTratamientoEditar.grid(row = 5, column=0, pady=3, padx=5, columnspan=2)

            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=65, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
            self.entryDetalleEditar.grid(row = 7, column=0, pady=3, padx=5, columnspan=2)

            self.svPrecioEditar = tk.StringVar()
            self.entryPrecioEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svPrecioEditar)
            self.entryPrecioEditar.config(width=65, font=("Verdana", 15), bg="#B2B4AC", selectbackground="#D1D2CD", selectforeground="black")
            self.entryPrecioEditar.grid(row = 9, column=0, pady=3, padx=5, columnspan=2)

            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(background="#777067")
            self.frameFechaEditar.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
                
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text="Fecha y Hora", width=30, font=("Verdana", 15,"bold"), background="#777067")
            self.lblFechaHistoriaEditar.grid(row=0, column=0, padx=5, pady=3)

            #  ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=("Verdana", 15), bg="#B2B4AC",selectbackground="#D1D2CD", selectforeground="black")
            self.entryFechaHistoriaEditar.grid(row = 0, column=1, pady=3, padx=5)

            #INSERTAR LOS VALORES A LOS ENTRYS

            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar) # 0 es la locación
            self.entryOperacionEditar.insert(0, self.operacionHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)
            self.entryPrecioEditar.insert(0, self.precioEditar)

            #BUTTON EDITAR HISTORIA
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text="Editar Historia", command = self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=("Verdana", 12,"bold"), background="#B2B4AC", cursor="hand2", activebackground="#D1D2CD")
            self.btnEditarHistoriaMedica.grid(row=1, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text="Salir", command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20, font=("Verdana", 12,"bold"), background="#B2B4AC", cursor="hand2", activebackground="#D1D2CD")
            self.btnSalirEditarHistoriaMedica.grid(row=1, column=1, padx=10, pady=5)

            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica

            self.idHistoriaMedica = None

        except:
            titulo = "Editar Historia"
            mensaje = "Error al editar historia"
            messagebox.showerror(titulo, mensaje)

    def historiaMedicaEditar(self):
        """Método que edita los historiales"""

        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svOperacionEditar.get(), self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.svPrecioEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.root.destroy()
            self.historiaMedica()
            
        except:
            titulo = "Editar Historia"
            mensaje = "Error al editar historia"
            messagebox.showerror(titulo, mensaje)
            self.topEditarHistoria.destroy()

################# LOGIN #########################

class Frame2(tk.Frame):
    """Clase ventana"""

    def __init__(self, login): 
        """Constructor de instancias"""
        super().__init__(login) 
        self.login = login
        self.intentosRegistrar=2
        self.intentosOlvidar=2
        self.intentosPrincipal=2
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

        self.Hyper=tk.Label(self)
        self.Hyper.configure(text="Visita nuestra página web", bg="#0E4C75", font=("Bahnschrift", 11, "underline", "bold"), fg="#BDE2FF", cursor="hand2")
        self.Hyper.place(x=510,y=645)
        self.Hyper.bind("<Button-1>",lambda x: webbrowser.open_new("https://hdjdudixjxy.github.io./"))
        self.Hyper.bind("<Enter>", self.EntrarColorHyper)
        self.Hyper.bind("<Leave>", self.SalirColorHyper)
        
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

        self.svUsuario_Existente=tk.StringVar()
        self.EntryUsuario_Existente=tk.Entry(self.frame1_2_1)
        self.EntryUsuario_Existente.configure(bg="#FFFFFF", font=("Bahnschrift", 30), width=17, textvariable=self.svUsuario_Existente)
        self.EntryUsuario_Existente.pack(side=tk.RIGHT, pady=10)

        self.imagenPassword=Image.open("ICONOS/password.png")
        self.imagenPassword=self.imagenPassword.resize((60,60), Image.ANTIALIAS)
        self.imgPassword=ImageTk.PhotoImage(self.imagenPassword)
        self.LblImagenPassword=tk.Label(self.frame1_2_2,image=self.imgPassword)
        self.LblImagenPassword.config(bg="#2A6C96", width=50, height=45)
        self.LblImagenPassword.pack(side=tk.LEFT, pady=20) 
        self.LblImagenPassword.pack_propagate(False)

        self.svContraseña_Existente=tk.StringVar()
        self.EntryContraseña_Existente=tk.Entry(self.frame1_2_2)
        self.EntryContraseña_Existente.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="*", width=17, textvariable=self.svContraseña_Existente)
        self.EntryContraseña_Existente.pack(side=tk.RIGHT, pady=20)
        

        self.frame1_2_3=tk.Frame(self.frame1_2)
        self.frame1_2_3.configure(bg="#3282B5")
        self.frame1_2_3.pack(fill=tk.BOTH, expand=True)

        self.svCheck=tk.BooleanVar()
        self.Check=tk.Checkbutton(self.frame1_2_3)
        self.Check.configure(text="Mostrar contraseña", font=("Bahnschrift",11),bg="#3282B5", activebackground="#3282B5", 
                            cursor="hand2",selectcolor="#2A6C96", variable=self.svCheck, command=self.mostrarContraseña)
        self.Check.pack(sid=tk.LEFT)

        self.frame1_2_4=tk.Frame(self.frame1_2)
        self.frame1_2_4.configure(bg="#3282B5",width=420,height=500)
        self.frame1_2_4.pack(padx=10, pady=10)

        self.Boton=tk.Button(self.frame1_2_4)
        self.Boton.configure(text="Login",font=("Bahnschrift", 20),bg="#BBE1F8",width=7, cursor="hand2", border=0, activebackground="#95B5C7", command=self.ejecutarApp)
        self.Boton.pack(side=tk.LEFT)
        self.Boton.bind("<Enter>",self.EntrarColorBoton)
        self.Boton.bind("<Leave>",self.SalirColorBoton)

        self.imagenLogin=Image.open("ICONOS/login.ico")
        self.imagenLogin=self.imagenLogin.resize((40,40), Image.ANTIALIAS)
        self.imgLogin=ImageTk.PhotoImage(self.imagenLogin)
        self.LblImagenLogin=tk.Label(self.frame1_2_4,image=self.imgLogin)
        self.LblImagenLogin.config(bg="#BBE1F8", width=50, height=50)
        self.LblImagenLogin.pack(side=tk.RIGHT) 
        self.LblImagenLogin.pack_propagate(False)
        self.LblImagenLogin.bind("<Enter>",self.EntrarColorBoton)
        self.LblImagenLogin.bind("<Leave>",self.SalirColorBoton)

        self.Label2=tk.Label(self.frame1_2)
        self.Label2.configure(text="¿Olvidaste la contraseña?", font=("Bahnschrift", 11), bg="#3282B5", fg="#BDE2FF",anchor="c", cursor="hand2")
        self.Label2.pack(pady=10)
        self.Label2.bind("<Button-1>",self.Login1)
        self.Label2.bind("<Enter>", self.EntrarColorLabel2)
        self.Label2.bind("<Leave>", self.SalirColorLabel2)

        self.Label3=tk.Label(self.frame1_2)
        self.Label3.configure(text="¿No tienes cuenta? REGÍSTRATE", font=("Bahnschrift", 11), bg="#3282B5", fg="#BDE2FF",anchor="c", cursor="hand2")
        self.Label3.pack()
        self.Label3.bind("<Button-1>",self.Login2)
        self.Label3.bind("<Enter>", self.EntrarColorLabel3)
        self.Label3.bind("<Leave>", self.SalirColorLabel3)

    def mostrarContraseña(self):
        """Método para mostrar * si el checkbutton está deshabilitado, si se habilita muestra el string ingresado"""

        if self.svCheck.get() == True:
            self.EntryContraseña_Existente.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="", width=17, textvariable=self.svContraseña_Existente)
        else:
            self.EntryContraseña_Existente.configure(bg="#FFFFFF", font=("Bahnschrift", 30), show="*", width=17, textvariable=self.svContraseña_Existente)

    def ejecutarApp(self):
        """Método para abrir la aplicación si es correcto el usuario y contraseña"""
        
        self.listaCondicionContraseña = listarCondicionLogin()
        self.listaCondicionContraseñaTRUE=[]            
        
        for p in range(len(self.listaCondicionContraseña)): 

            self.listaCondicionContraseña2=self.listaCondicionContraseña[p]
            self.listaCondicionContraseñaTRUE.append(self.listaCondicionContraseña2[0])

        self.listaCondicionUsuario = listarCondicionLogin2()
        self.listaCondicionUsuarioTRUE=[]            
        
        for p in range(len(self.listaCondicionUsuario)): 

            self.listaCondicionUsuario2=self.listaCondicionUsuario[p]
            self.listaCondicionUsuarioTRUE.append(self.listaCondicionUsuario2[0])    
        
        if self.svUsuario_Existente.get() in self.listaCondicionUsuarioTRUE:
            
            if self.svContraseña_Existente.get() in self.listaCondicionContraseñaTRUE:
                
                self.LblImagenLogin.config(bg="#95B5C7", width=50, height=50)
                self.login.destroy()
                aplicacion = tk.Tk() 
                aplicacion.title("HISTORIAS CLINICAS") # nombre de la interfaz
                aplicacion.resizable(width=False, height=False) # expansión a pantalla completa
                aplicacion.geometry("1420x730+48+40") # tamaño por defecto y posición
                aplicacion.minsize(width=1280, height=720) # tamaño mínimo al minimizar
                aplicacion.iconbitmap("ICONOS/ICONO.ico")
                fondo = Frame(aplicacion) # ventana para dar color de fondo
                fondo.mainloop() # bucle generador
            
            else:
                
                self.intentosPrincipal-=1

                if self.intentosPrincipal>0:

                    messagebox.showwarning("ADVERTENCIA",f"""Contraseña incorrecta, vuelve a intentarlo.
Te quedan {self.intentosPrincipal} intento""")

                else:

                    messagebox.showerror("ERROR", "Contraseña incorrecta")
                    self.bind('<Motion>', self.NoEjecutar)
                    self.frame1.bind('<Motion>', self.NoEjecutar)
                    self.frame2.bind('<Motion>', self.NoEjecutar)
                    self.frame1_1.bind('<Motion>', self.NoEjecutar)
                    self.frame1_2.bind('<Motion>', self.NoEjecutar)

        else:

            messagebox.showerror("ERROR", "Este usuario no existe, porfavor registrese")

    def NoEjecutar(self,event):
        """Evento que colocará el cursor en una posición absoluta de la pantalla, el botón cerrar de la ventana"""

        mouse.move(1231, 39, absolute=True, duration=0.03)

    def EntrarColorBoton(self,event):
        self.Boton.configure(text="Login",font=("Bahnschrift", 20),bg="#A3C5D9",width=7, cursor="hand2", border=0, activebackground="#95B5C7", command=self.ejecutarApp)
        self.LblImagenLogin.config(bg="#A3C5D9", width=50, height=50)

    def SalirColorBoton(self,event):
        self.Boton.configure(text="Login",font=("Bahnschrift", 20),bg="#BBE1F8",width=7, cursor="hand2", border=0, activebackground="#95B5C7", command=self.ejecutarApp)
        self.LblImagenLogin.config(bg="#BBE1F8", width=50, height=50)

    def EntrarColorHyper(self,event):
        self.Hyper.configure(text="Visita nuestra página web", bg="#0E4C75", font=("Bahnschrift", 11, "underline", "bold"), fg="#A4C3DA", cursor="hand2")
        
    def SalirColorHyper(self,event):
        self.Hyper.configure(text="Visita nuestra página web", bg="#0E4C75", font=("Bahnschrift", 11, "underline", "bold"), fg="#BDE2FF", cursor="hand2")

    def EntrarColorLabel2(self,event):
        self.Label2.configure(text="¿Olvidaste la contraseña?", font=("Bahnschrift", 11), bg="#3282B5", fg="#A4C3DA",anchor="c", cursor="hand2")
    
    def SalirColorLabel2(self,event):
        self.Label2.configure(text="¿Olvidaste la contraseña?", font=("Bahnschrift", 11), bg="#3282B5", fg="#BDE2FF",anchor="c", cursor="hand2")

    def EntrarColorLabel3(self,event):
        self.Label3.configure(text="¿No tienes cuenta? REGÍSTRATE", font=("Bahnschrift", 11), bg="#3282B5", fg="#A4C3DA",anchor="c", cursor="hand2")

    def SalirColorLabel3(self,event):
        self.Label3.configure(text="¿No tienes cuenta? REGÍSTRATE", font=("Bahnschrift", 11), bg="#3282B5", fg="#BDE2FF",anchor="c", cursor="hand2")

    ######### OLVIDAR CONTRASEÑA ##########

    def TablaLogin(self):
        """Método que muestra todos los Trabajadores, sus usuarios y contraseñas en un Treeview"""

        try:

            self.ListaLogin = listarLogin()
            self.ListaLogin.reverse()
            self.tablaLogin = ttk.Treeview(self.topLogin1, column=("Trabajador", "Usuario", "Contraseña"))
            self.tablaLogin.config(height=10)
            self.tablaLogin.tag_configure("evenrow", background="oldlace")
            self.tablaLogin.grid(column=0, row=0, columnspan=3,sticky="nse")

            self.scroll=ttk.Scrollbar(self.topLogin1, orient="vertical", command=self.tablaLogin.yview)
            self.scroll.grid(row=0, column=3, sticky="nse")

            self.tablaLogin.configure(yscrollcommand=self.scroll.set)

            self.tablaLogin.heading("#0",text="ID")
            self.tablaLogin.heading("#1",text="Trabajador")
            self.tablaLogin.heading("#2",text="Usuario")
            self.tablaLogin.heading("#3",text="Contraseña")

            self.tablaLogin.column("#0", anchor=W, width=50)
            self.tablaLogin.column("#1", anchor=W, width=250)
            self.tablaLogin.column("#2", anchor=W, width=125)
            self.tablaLogin.column("#3", anchor=W, width=125)


            for p in self.ListaLogin:
                self.tablaLogin.insert("",0,text=p[0], values=(p[1],p[2],p[3]), tags=("evenrow",))

        except:
            
            titulo = "Usuarios"
            mensaje = "Error al mostrar los usuarios"
            messagebox.showerror(titulo, mensaje)

    def Login1(self, event):
        """Evento para generar el Top Level donde se ingresará la clave al darle olvide mi contraseña"""

        if self.intentosOlvidar>0:

            self.topCorroborar1=Toplevel()
            self.topCorroborar1.title("CLAVE SECRETA")
            self.topCorroborar1.geometry("630x120+160+260")
            self.topCorroborar1.resizable(width=False, height=False)
            self.topCorroborar1.iconbitmap("ICONOS/incognito2.ico")
            self.topCorroborar1.configure(bg="#0E4C75")

            self.LabelClave1=tk.Label(self.topCorroborar1)
            self.LabelClave1.configure(text="Ingresa la clave para ver los usuarios", font=("Bahnschrift", 20), bg="#0E4C75", fg="#BDE2FF")
            self.LabelClave1.pack(pady=10)

            self.svclave1=tk.StringVar()
            self.entryClave1=tk.Entry(self.topCorroborar1)
            self.entryClave1.configure(textvariable=self.svclave1, font=("Bahnschrift", 20), show="*")
            self.entryClave1.pack()
            self.entryClave1.bind("<Return>",self.LoginVerUsuarios) # Dando ENTER ejecutamos LoginVerUsuarios

        else:
            self.topCorroborar1.destroy()
            messagebox.showwarning("ADVERTENCIA","No vuelva a intentarlo o será despedido!")

    def LoginVerUsuarios(self,event):
        """Evento que muestra el top que contiene la tabla de usuarios si se cumple el if de la clave"""

        if self.svclave1.get() == "Edwin":

            self.topCorroborar1.destroy()
            self.topLogin1 = Toplevel()
            self.topLogin1.title("USUARIOS")
            self.topLogin1.geometry("570x227+160+260")
            self.topLogin1.resizable(width=False, height=False)
            self.topLogin1.iconbitmap("ICONOS/incognito2.ico")
            
            self.TablaLogin() 
        
        else:
            self.intentosOlvidar-=1

            if self.intentosOlvidar>0:

                messagebox.showerror("ERROR",f"""Clave incorrecta, vuelve a intentarlo.
Te quedan {self.intentosOlvidar} intento""")

                self.topCorroborar1.iconify()
                self.topCorroborar1.deiconify()
            else:

                self.topCorroborar1.destroy()
                messagebox.showwarning("ADVERTENCIA","Pónganse en contacto con el administrador, no reintente buscar su contraseña")

    ########## REGÍSTRATE ##########

    def Login2(self, event):
        """Evento para generar el Top Level donde se ingresará la clave al darle Registrate"""

        if self.intentosRegistrar>0:

            self.topCorroborar2=Toplevel()
            self.topCorroborar2.title("CLAVE SECRETA")
            self.topCorroborar2.geometry("630x120+160+260")
            self.topCorroborar2.resizable(width=False, height=False)
            self.topCorroborar2.iconbitmap("ICONOS/incognito2.ico")
            self.topCorroborar2.configure(bg="#0E4C75")

            self.LabelClave2=tk.Label(self.topCorroborar2)
            self.LabelClave2.configure(text="Ingresa la clave para ver los usuarios", font=("Bahnschrift", 20), bg="#0E4C75", fg="#BDE2FF")
            self.LabelClave2.pack(pady=10)

            self.svclave2=tk.StringVar()
            self.entryClave2=tk.Entry(self.topCorroborar2)
            self.entryClave2.configure(textvariable=self.svclave2, font=("Bahnschrift", 20),show="*")
            self.entryClave2.pack()
            self.entryClave2.bind("<Return>",self.LoginRegistrate) # Dando ENTER ejecutamos LoginVerUsuarios

        else:

            self.topCorroborar2.destroy()
            messagebox.showwarning("ADVERTENCIA","Para evitar problemas legales, porfavor no vuelva a intentarlo")

    def LoginRegistrate(self,event):
        """Evento que muestra el top para agregar un usuario si es correcta la clave"""

        if self.svclave2.get() == "Edwin":

            self.topCorroborar2.destroy()

            self.topLogin2 = Toplevel()
            self.topLogin2.title("USUARIOS")
            self.topLogin2.geometry("570x200+160+260")
            self.topLogin2.resizable(width=False, height=False)
            self.topLogin2.iconbitmap("ICONOS/incognito2.ico")
            self.topLogin2.configure(bg="#0E4C75")
            
            self.ventana1=tk.Frame(self.topLogin2)
            self.ventana1.configure(bg="#0E4C75",width=570, height=30)
            self.ventana1.pack(pady=10)
            self.ventana1.pack_propagate(False)

            self.ventana2=tk.Frame(self.topLogin2)
            self.ventana2.configure(bg="#0E4C75",width=570, height=30)
            self.ventana2.pack(pady=10)
            self.ventana2.pack_propagate(False)

            self.ventana3=tk.Frame(self.topLogin2)
            self.ventana3.configure(bg="#0E4C75",width=570, height=30)
            self.ventana3.pack(pady=10)
            self.ventana3.pack_propagate(False)

            self.ventana4=tk.Frame(self.topLogin2)
            self.ventana4.configure(bg="#0E4C75")
            self.ventana4.pack(pady=10)

            ########## CLASES ENTRYS ################

            self.svTrabajador=tk.StringVar()
            self.entry=tk.Entry(self.ventana1)
            self.entry.configure(textvariable=self.svTrabajador, font=("Bahnschrift", 15), width=22)
            self.entry.pack(side=tk.RIGHT, padx=6)

            self.svUsuario_Agregar=tk.StringVar()
            self.entry2=tk.Entry(self.ventana2)
            self.entry2.configure(textvariable=self.svUsuario_Agregar, font=("Bahnschrift", 15), width=22)
            self.entry2.pack(side=tk.RIGHT, padx=6)

            self.svContraseña_Agregar=tk.StringVar()
            self.entry3=tk.Entry(self.ventana3)
            self.entry3.configure(textvariable=self.svContraseña_Agregar, font=("Bahnschrift", 15), width=22)
            self.entry3.pack(side=tk.RIGHT, padx=6)

            ########## CLASES LABELS ############

            self.LabelTrabajador=tk.Label(self.ventana1)
            self.LabelTrabajador.configure(text="Ingrese sus nombres y apellidos", font=("Bahnschrift", 15),bg="#0E4C75", justify=tk.LEFT, fg="#BDE2FF")
            self.LabelTrabajador.pack(side=tk.LEFT, padx=2)

            self.LabelUsuario=tk.Label(self.ventana2)
            self.LabelUsuario.configure(text="Ingrese un nombre de usuario", font=("Bahnschrift", 15),bg="#0E4C75", justify=tk.LEFT, fg="#BDE2FF")
            self.LabelUsuario.pack(side=tk.LEFT, padx=2)

            self.LabelContraseña=tk.Label(self.ventana3)
            self.LabelContraseña.configure(text="Ingrese una contraseña", font=("Bahnschrift", 15),bg="#0E4C75", justify=tk.LEFT, fg="#BDE2FF")
            self.LabelContraseña.pack(side=tk.LEFT, padx=2)

            ######## CLASE BUTTON #############
    
            self.Boton2=tk.Button(self.ventana4)
            self.Boton2.configure(text="AGREGAR", bg="#BBE1F8",font=("Bahnschrift", 12), width=8, cursor="hand2", border=0, activebackground="#A3C5D9", command=self.Registrar)
            self.Boton2.pack()

        else:
            self.intentosRegistrar-=1

            if self.intentosRegistrar>0:

                messagebox.showerror("ERROR",f"""Clave incorrecta, vuelve a intentarlo.
Te quedan {self.intentosRegistrar} intento""")

                self.topCorroborar2.iconify()
                self.topCorroborar2.deiconify()
            
            else:

                self.topCorroborar2.destroy()
                messagebox.showwarning("ADVERTENCIA","Pónganse en contacto con el administrador, no reintente registrarse otra vez")
        
    def Registrar(self):
        """Método que guarda en la clase Login"""

        self.listaCondicionUsuario_Registrar = listarCondicionLogin2()
        self.listaCondicionUsuario_RegistrarTRUE=[]            
        
        for p in range(len(self.listaCondicionUsuario_Registrar)): 

            self.listaCondicionUsuario_Registrar2=self.listaCondicionUsuario_Registrar[p]
            self.listaCondicionUsuario_RegistrarTRUE.append(self.listaCondicionUsuario_Registrar2[0])
        
        if  self.svUsuario_Agregar.get() in self.listaCondicionUsuario_RegistrarTRUE:

            messagebox.showinfo("ADVERTENCIA", "Este nombre de usuario ya existe")
            self.topLogin2.destroy()
            self.LoginRegistrate(self)

        else:

            guardarLogin(self.svTrabajador.get(), self.svUsuario_Agregar.get(), self.svContraseña_Agregar.get())
            self.topLogin2.destroy()
        
#################### ERROR INTERFAZ ##########################

def error():
    """Interfaz para mostrar error"""
    
    AppError = tk.Tk()
    AppError.title("¡Vaya!")
    AppError.geometry("350x200+600+200") # resolución por defecto
    AppError.iconbitmap("ICONOS/error2.ico")
    AppError.resizable(width=False, height=False) # ponemos que se pueda agrandar?
    AppError.configure(background="steelblue1")

###################################################
    
    LbError = tk.Label(AppError,
        text="HA OCURRIDO UN ERROR",
        font=("Arial", 18, "bold"),
        foreground="red2",
        background="steelblue1"
    )

    LbError.place(x=25, y=60)

############################################################

    LbError2 = tk.Label(AppError,
        text="Vuelva a ejecutar la aplicación",
        font=("Arial", 12),
        foreground="gray30",
        background="steelblue1"
    )

    LbError2.place(x=74, y=97)

###############################################################
    AppError.deiconify()
    AppError.mainloop()