from CONEXION.PacienteDao import DatosPaciente, editarDatoPaciente, guardarDatoPaciente, listar, listarCondicion, eliminarPaciente
from CONEXION.HistorialDao import guardarHistoria, editarHistoria, eliminarHistoria, listarHistoria
import tkinter as tk
from tkinter import W, ttk, messagebox, Toplevel
import tkcalendar as tc
import datetime
from PIL import Image, ImageTk
import fpdf


################## VENTANA DE FONDO ##########################

class Frame(tk.Frame):
    """Clase ventana"""

    def __init__(self, aplicacion): 
        """Constructor de instancias"""

        super().__init__(aplicacion) # utilizamos super() para llevar a cabo herencias múltiples, de las subclases a la superclase
        self.aplicacion = aplicacion
        self.pack(fill=tk.BOTH, expand=True)
        self.config(background="lightseagreen")
        self.idPersona = None
        self.idPersonaHistoria=None
        self.idHistoriaMedica=None
        self.idHistoriaMedicaEditar=None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

################## WIDGETS DE LA VENTANA PRINCIPAL ######################

    def camposPaciente(self):
        
        ##################### LABELS ##########################

        self.lblNombre = tk.Label(self, text="NOMBRE COMPLETO: ")
        self.lblNombre.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblNombre.grid(column=0, row=0, pady=5)

        self.lblApellidos = tk.Label(self, text="APELLIDOS COMPLETOS: ")
        self.lblApellidos.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblApellidos.grid(column=0,row=1, pady=5)

        self.lblDni = tk.Label(self, text="DNI: ")
        self.lblDni.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblDni.grid(column=0,row=2, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text="FECHA DE NACIMIENTO: ")
        self.lblFechNacimiento.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblFechNacimiento.grid(column=0,row=3, pady=5)

        self.lblEdad = tk.Label(self, text="EDAD: ")
        self.lblEdad.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblEdad.grid(column=0,row=4, pady=5)

        self.lblTelefono = tk.Label(self, text="TELÉFONO: ")
        self.lblTelefono.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblTelefono.grid(column=0,row=5, pady=5) 

        self.lblCorreo = tk.Label(self, text="CORREO ELECTRÓNICO: ")
        self.lblCorreo.config(font=("verdana",15,"bold"), background="lightseagreen", anchor = "w")
        self.lblCorreo.grid(column=0,row=6, pady=5)

        ######################### ENTRYS ###############################

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=("verdana",15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellidos = tk.StringVar()
        self.entryApellidos = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApellidos.config(width=50, font=("verdana",15))
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=("verdana",15))
        self.entryDni.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=("verdana",15))
        self.entryFecNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=("verdana",15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=("verdana",15))
        self.entryTelefono.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=("verdana",15))
        self.entryCorreo.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        ######################### BUTTONS ####################################

        self.btnNuevo = tk.Button(self, text="NUEVO", command=self.habilitar)
        self.btnNuevo.config(width=20, font=("verdana",12,"bold"), 
                                background="firebrick1", cursor="hand2",activebackground="firebrick3")
        self.btnNuevo.grid(column=0,row=7, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text="GUARDAR", command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=("verdana",12,"bold"), 
                                background="sienna1", cursor="hand2",activebackground="sienna3")
        self.btnGuardar.grid(column=1,row=7, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text="CANCELAR")
        self.btnCancelar.config(width=20, font=("verdana",12,"bold"), 
                                background="khaki1", cursor="hand2",activebackground="khaki3")
        self.btnCancelar.grid(column=2,row=7, padx=10, pady=5)

        self.btnCalendario = tk.Button(self, text="BUSCAR")
        self.btnCalendario.config(width=13, font=("verdana",12,"bold"), command=self.MostrarCalendario,
                                background="darkolivegreen1", cursor="hand2",activebackground="darkolivegreen3")
        self.btnCalendario.grid(column=3,row=3,padx=10,pady=5)

        #################### WDGETS DEL BUSCADOR ########################
        
        self.lblBuscarDni = tk.Label(self, text="Buscar DNI: ")
        self.lblBuscarDni.config(font=("verdana",15,"bold"), bg="lightseagreen")
        self.lblBuscarDni.grid(column=3, row=0, padx=2, pady=5)

        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=("verdana",15))
        self.entryBuscarDni.grid(column=4, row=0, padx=2, pady=5)

        self.btnBuscarCondicion = tk.Button(self, text="BUSCAR", command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=10, font=("verdana",12,"bold"), 
                                bg="purple1", cursor="hand2",activebackground="purple3")
        self.btnBuscarCondicion.grid(column=4,row=1, padx=2, pady=5)

        ####################### IMAGEN ####################

        self.imagen=Image.open("ICONOS/UNT.png")
        self.imagen=self.imagen.resize((220,180), Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(self.imagen)
        self.LblImagen=tk.Label(self,image=self.img)
        self.LblImagen.config(bg="lightseagreen")
        self.LblImagen.grid(column=4,row=2,rowspan=5, columnspan=2)

################ FUNCIONES PARA LA VENTANA PRINCIPAL  ###################
            
    def deshabilitar(self):
        """Función que bloquea los entrys, para después habilitarlos con el botón NUEVO"""

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
        """Función para habilitar los entrys"""

        self.svNombre.set("")
        self.svApellidos.set("")
        self.svDni.set("")
        self.svFecNacimiento.set("")
        self.svEdad.set("")
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
        """Función para el entry buscar por DNI"""

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
        """Función que inserta la tabla treeView de ttk en la GUI de tkinter"""

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

        self.tabla.tag_configure("evenrow", background="antiquewhite1") # damos color a las filas

        #definimos los títulos de cada columna

        self.tabla.heading("#0",text="ID")
        self.tabla.heading("#1",text="Nombres")
        self.tabla.heading("#2",text="Apellidos")
        self.tabla.heading("#3",text="DNI")
        self.tabla.heading("#4",text="F. Nacimiento")
        self.tabla.heading("#5",text="Edad")
        self.tabla.heading("#6",text="Telefono")
        self.tabla.heading("#7",text="Correo")

        self.tabla.column("#0", anchor=W, width=3)
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
        self.btnEditarPaciente.config(width=20,font=("verdana",12,"bold"), bg="orange", activebackground="darkorange", cursor="hand2")
        self.btnEditarPaciente.grid(row=9, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text="Eliminar Paciente", command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=("verdana",12,"bold"), bg="cornflowerblue", activebackground="royalblue2", cursor="hand2")
        self.btnEliminarPaciente.grid(row=9, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text="Historial Paciente", command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=50,font=("verdana",12,"bold"), bg="cyan2", activebackground="cyan3", cursor="hand2")
        self.btnHistorialPaciente.grid(row=9, column=2, columnspan=3, pady=5)

################# FUNCIONES DEL CALENDARIO ###################

    def MostrarCalendario(self):
        """Función que muestra el calendario en la interfaz"""

        self.topCalendario = Toplevel() #Creamos una ventana flotante
        self.topCalendario.title("FECHA DE NACIMIENTO")
        self.topCalendario.geometry("300x300+1000+80")
        self.topCalendario.resizable(width=False, height=False)
        self.topCalendario.iconbitmap("ICONOS/calendario.ico")
        self.topCalendario.config(background="lightseagreen")

        self.calendar = tc.Calendar(self.topCalendario, selectmode="day", year=1990, month=3, day=20,locale ="es_US", background="burlywood4", foreground="gray2", bordercolor="burlywood3", headersbackground="burlywood3",headersforeground="gray2",selectbackground="burlywood2", selectforeground="gray2",normalbackground="burlywood1",normalforeground="gray2",weekendbackground="burlywood1",weekendforeground="gray2", othermonthbackground="wheat3", othermonthforeground="gray2", othermonthwebackground="wheat3", othermonthweforeground="gray2", cursor = "hand2", date_pattern="dd/mm/Y")
        self.calendar.pack(fill=tk.BOTH, expand=True)

        self.btnCalendario2 = tk.Button(self.topCalendario, text="INSERTAR")
        self.btnCalendario2.config(width=13, font=("verdana",12,"bold"), command=self.EnviarFecha,
                                background="navajowhite3", cursor="hand2",activebackground="navajowhite4")
        self.btnCalendario2.pack(fill=tk.BOTH)

    def EnviarFecha(self):
        """Función que envía la fecha de self.calendar al entry FecNacimiento y referencia a la función calcularEdad"""

        self.svFecNacimiento.set(self.calendar.get_date()) # Mediante set mandamos la fecha al entry y con get_date la obtenemos de self.calendar 

        if len(self.calendar.get_date())>1: # Condición para referenciar la función CalcularEdad
            self.CalcularEdad() 

    def CalcularEdad(self): 
        """Función que inserta la edad en el entry Edad, restando el año obtenido con el modulo datetime y el ingresado por self.calendar"""

        self.fechaActual = datetime.date.today()
        self.date1 = self.calendar.get_date()
        self.convertidor = datetime.datetime.strptime(self.date1, "%d/%m/%Y") # Retorna datetime correspondiente a self.date1, analizado según format
        # Se usa strptime, porque necesitamos que sea compatible con el módulo datetime, ya que fue generado por tkcalendar

        self.resultado = self.fechaActual.year - self.convertidor.year
        self.svEdad.set(self.resultado)

############## FUNCIONES QUE VINCULAN LOS OBJETOS #############

    def guardarPaciente(self):
        """Función para insertar los datos del paciente a la base de datos"""

        persona = DatosPaciente(self.svNombre.get(), self.svApellidos.get(), self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(),self.svTelefono.get(), self.svCorreo.get())
        # el metodo get lee lo que se inserta en los entrys

        if self.idPersona == None: # si el id no tiene valor, entonces guarda el dato, sino solo lo vamos a editar
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        self.deshabilitar() # una vez presionado el boton duardar, se va a borrar todos los datos de los entrys
        self.tablaPaciente() # para actualizar la tabla cuando se ingresan datos
    
    def editarPaciente(self):
        """Función que cambia los datos, pero en la tabla de la GUI"""

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
        """Función que elimina los pacientes de la tabla y no de la base de datos"""

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
        """función que muestra todos los historiales del paciente en un Treeview"""
        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())["text"]
                self.idPersonaHistoria = self.idPersona

            if self.idPersona > 0:

                idPersona = self.idPersona

            self.ListaHistoria = listarHistoria(idPersona)
            self.tabla2 = ttk.Treeview(self.topHistoriaMedica, column=("Paciente", "FechaHistoria", "MotivoDeLaVisita", "Operacion", "Tratamiento", "DetalleAdicional"))
            self.tabla2.config(height=10)
            self.tabla2.tag_configure("evenrow", background="oldlace")
            self.tabla2.grid(column=0, row=0, columnspan=7,sticky="nse")

            self.scroll2=ttk.Scrollbar(self.topHistoriaMedica, orient="vertical", command=self.tabla2.yview)
            self.scroll2.grid(row=0, column=7, sticky="nse")

            self.tabla2.configure(yscrollcommand=self.scroll2.set)

            self.tabla2.heading("#0",text="ID")
            self.tabla2.heading("#1",text="Paciente")
            self.tabla2.heading("#2",text="Fecha y Hora")
            self.tabla2.heading("#3",text="Motivo de la visita")
            self.tabla2.heading("#4",text="Operacion")
            self.tabla2.heading("#5",text="Tratamiento")
            self.tabla2.heading("#6",text="Detalle adicional")

            self.tabla2.column("#0", anchor=W, width=40)
            self.tabla2.column("#1", anchor=W, width=200)
            self.tabla2.column("#2", anchor=W, width=150)
            self.tabla2.column("#3", anchor=W, width=200)
            self.tabla2.column("#4", anchor=W, width=150)
            self.tabla2.column("#5", anchor=W, width=300)
            self.tabla2.column("#6", anchor=W, width=450)

            for p in self.ListaHistoria:
                self.tabla2.insert("",0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]), tags=("evenrow",))

        except:
            
            titulo = "Historia Medica"
            mensaje = "Error al mostrar historial"
            messagebox.showerror(titulo, mensaje)
            self.idPersona = None

    def historiaMedica(self):
        """Función para generar el Top Level donde estará la tabla de los historiales del paciente"""

        self.topHistoriaMedica = Toplevel()
        self.topHistoriaMedica.title("HISTORIAL MEDICO")
        self.topHistoriaMedica.geometry("1515x280+5+50")
        self.topHistoriaMedica.resizable(width=False, height=False)
        self.topHistoriaMedica.iconbitmap("ICONOS/Historial.ico")
        self.topHistoriaMedica.config(background="azure")
        
        self.tablaHistoria() 

        self.btnGuardarHistoria=tk.Button(self.topHistoriaMedica, text="Agregar Historia", command=self.topAgregarHistoria)
        self.btnGuardarHistoria.config(width=20, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="seagreen1", activebackground="seagreen3", cursor="hand2")
        self.btnGuardarHistoria.grid(column=0, row=1, padx=10, pady=10)

        self.btnEditarHistoria=tk.Button(self.topHistoriaMedica, text="Editar Historia",command=self.topEditarHistorialMedico)
        self.btnEditarHistoria.config(width=20, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="salmon2", activebackground="salmon4", cursor="hand2")
        self.btnEditarHistoria.grid(column=1, row=1, padx=10, pady=10)

        self.btnEliminarHistoria=tk.Button(self.topHistoriaMedica, text="Eliminar Historia", command=self.eliminarHistorialMedico)
        self.btnEliminarHistoria.config(width=20, font=("Verdana", 12, "bold"),
                                        foreground="gray2", background="purple2", activebackground="purple4", cursor="hand2")
        self.btnEliminarHistoria.grid(column=2, row=1, padx=10, pady=10)

        self.btnEnviar=tk.Button(self.topHistoriaMedica, text="Generar PDF",command=self.crearPDF)
        self.btnEnviar.config(width=20,font=("Verdana", 12, "bold"), foreground="gray2",
                                    background="tomato2", activebackground="tomato3", cursor="hand2")
        self.btnEnviar.grid(column=3, row=1,padx=10,pady=10)

        self.idPersona = None
        

    def crearPDF(self):
        """función para crear el historial de cada paciente"""
        
        pdf=fpdf.FPDF(orientation="L",unit="mm",format="A4")
        pdf.add_page()
        
        id=self.tabla2.item(self.tabla2.selection())["text"]
        n=self.tabla2.item(self.tabla2.selection())["values"][0]
        f=self.tabla2.item(self.tabla2.selection())["values"][1]
        a=self.tabla2.item(self.tabla2.selection())["values"][2]
        b=self.tabla2.item(self.tabla2.selection())["values"][3]
        c=self.tabla2.item(self.tabla2.selection())["values"][4]
        d=self.tabla2.item(self.tabla2.selection())["values"][5]
        g=str(self.tabla.item(self.tabla.selection())["values"][2])

        pdf.set_font("Arial","",14)
        pdf.text(x=230,y=10, txt = "Generado el: "+str(datetime.date.today()))
        pdf.text(x=130, y=200, txt = "Trujillo-PERÚ")

        pdf.image("ICONOS/UNT.png", x=250, y=15, w=40, h=35)
        pdf.image("ICONOS/vigo.png", x=45, y=160, w=40, h=20)
        pdf.image("ICONOS/jonathan.png", x=130, y=160, w=40, h=20)
        pdf.image("ICONOS/victor.png", x=215, y=160, w=40, h=20)

        pdf.set_font("Arial","B",20) 
        pdf.text(x=125, y=15, txt="CLÍNICA UNT")

        pdf.set_font("Arial","B",16)
        pdf.text(x=10, y=35, txt="Paciente:")
        pdf.text(x=10, y=50, txt="DNI:")
        pdf.text(x=10, y=65, txt="Motivo de la visita a la clínica:")
        pdf.text(x=10, y=80, txt="Fecha y hora de la visita:")
        pdf.text(x=10, y=95, txt="Su operación fue:")
        pdf.text(x=10, y=110, txt="Debe seguir el siguiente tratamiento:")
        pdf.text(x=10, y=125, txt="Detalles adicionales:")

        pdf.set_font("Arial","",16)
        pdf.text(x=40, y=35, txt=n)
        pdf.text(x=30, y=50, txt=g)
        pdf.text(x=100, y=65, txt=a)
        pdf.text(x=90, y=80, txt=f)
        pdf.text(x=70, y=95, txt=b)
        pdf.text(x=120, y=110, txt=c)
        pdf.text(x=80, y=125, txt=d)

        pdf.set_font("Arial","B",14)
        pdf.text(x=35,y=180, txt="Vigo Villar Cristhian A.")
        pdf.text(x=117,y=180, txt="Sanchez Rojas Jonathan A.") 
        pdf.text(x=200,y=180, txt="Valdiviezo Jimenez Victor J.")

        pdf.set_font("Arial","",14)
        pdf.text(x=50, y=185, txt="Cirujano")
        pdf.text(x=137, y=185, txt="Pediatra")
        pdf.text(x=220, y=185, txt="Traumatólogo")

        pdf.output(f"HISTORIALES_PDF/Historial_{id}_{n}.pdf")
      
    def topAgregarHistoria(self):
        """Función para generar el Top Level donde agregaremos los datos del historial"""

        self.topAHistoria = tk.Toplevel()
        self.topAHistoria.title("AGREGAR HISTORIA")
        self.topAHistoria.geometry("900x450+300+350")
        self.topAHistoria.resizable(width=False, height=False)
        self.topAHistoria.iconbitmap("ICONOS/ICONO.ico")
        self.topAHistoria.config(background="cornsilk2")

        ##################### FRAME 1 ##########################

        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(background="cornsilk2")
        self.frameDatosHistoria.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)

            ##################### LABELS-F1 ##########################

        self.lblMotivo = tk.Label(self.frameDatosHistoria, text="Motivo de la visita", width=30, font=("Verdana", 15,"bold"), background="cornsilk2")
        self.lblMotivo.grid(row=0, column=0, padx=5, pady=3)

        self.lblOperacion = tk.Label(self.frameDatosHistoria, text="Operación", width=20, font=("Verdana", 15,"bold"), background="cornsilk2")
        self.lblOperacion.grid(row=2, column=0, padx=5, pady=3)
        
        self.lblTratamiento = tk.Label(self.frameDatosHistoria, text="Tratamiento", width=20, font=("Verdana", 15,"bold"), background="cornsilk2")
        self.lblTratamiento.grid(row=4, column=0, padx=5, pady=3)

        self.lblDetalle = tk.Label(self.frameDatosHistoria, text="Detalle adicional", width=30, font=("Verdana", 15,"bold"), background="cornsilk2")
        self.lblDetalle.grid(row=6, column=0, padx=5, pady=3)

            ##################### ENTRYS-F1 ##########################

        self.svMotivo = tk.StringVar()
        self.Motivo = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivo)
        self.Motivo.config(width=64, font=("Verdana", 15))
        self.Motivo.grid(row=1, column=0, padx= 5, pady=3, columnspan=2)

        self.svOperacion = tk.StringVar()
        self.Operacion = tk.Entry(self.frameDatosHistoria, textvariable=self.svOperacion)
        self.Operacion.config(width=64, font=("Verdana", 15))
        self.Operacion.grid(row=3, column=0, padx= 5, pady=3, columnspan=2)

        self.svTratamiento = tk.StringVar()
        self.Tratamiento = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamiento)
        self.Tratamiento.config(width=64, font=("Verdana", 15))
        self.Tratamiento.grid(row=5, column=0, padx= 5, pady=3, columnspan=2)

        self.svDetalle = tk.StringVar()
        self.Detalle = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalle)
        self.Detalle.config(width=64, font=("Verdana", 15))
        self.Detalle.grid(row=7, column=0, padx= 5, pady=3, columnspan=2)

        ##################### FRAME 2 ##########################

        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg="cornsilk2")
        self.frameFechaHistoria.pack(fill=tk.BOTH, expand=True, padx=20,pady=10)

            ##################### LABELS-F2 ##########################

        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text="Fecha y Hora", width=20, font=("Verdana", 15,"bold"), background="cornsilk3")
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        
            ##################### ENTRYS-F2 ##########################

        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=("Verdana", 15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        
            ##################### FECHA Y HORA-F2 ####################

        xFecha=str(datetime.date.today().strftime("%d/%m/%Y, "))
        xHora=str(datetime.datetime.now().strftime("%I:%M %p"))
        self.svFechaHistoria.set(xFecha+xHora) 


            ##################### BUTTONS-F2 ##########################

        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Agregar", command=self.agregaHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=("Verdana", 12,"bold"), foreground="ghostwhite", background="lightsalmon", cursor="hand2", activebackground="salmon")
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text="Salir",command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=("Verdana", 12,"bold"), foreground="ghostwhite", background="gray6", cursor="hand2", activebackground="gray2")
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

        self.idPersona = None

    def agregaHistorialMedico(self):
        """Función que agrega los historiales"""

        try:
            if self.idHistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(),self.svMotivo.get(), self.svOperacion.get(), self.svTratamiento.get(),self.svDetalle.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.historiaMedica()
            self.idPersona = None

        except:
            titulo = "Agregar Historia"
            mensaje = "Error al agregar historia Medica"
            messagebox.showerror(titulo, mensaje)

    def eliminarHistorialMedico(self):
        """función que elimina los historiales, de forma definitiva"""

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
        
        try:
            self.idHistoriaMedica = self.tabla2.item(self.tabla2.selection())["text"]
            self.fechaHistoriaEditar = str(datetime.date.today().strftime("%d/%m/%Y, ") + datetime.datetime.now().strftime("%I:%M %p"))
            self.motivoHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][2]
            self.operacionHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][3]
            self.tratamientoHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][4]
            self.detalleHistoriaEditar = self.tabla2.item(self.tabla2.selection())["values"][5]

            self.topEditarHistoria = tk.Toplevel()
            self.topEditarHistoria.geometry("910x450+300+350")
            self.topEditarHistoria.title("EDITAR HISTORIA MEDICA")
            self.topEditarHistoria.resizable(width=False, height=False)
            self.topEditarHistoria.iconbitmap("ICONOS/ICONO.ico")
            self.topEditarHistoria.config(background="palegreen")

            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(background="palegreen")
            self.frameEditarHistoria.pack(fill=tk.BOTH, expand=True, padx=20,pady=10)

            #LABEL EDITAR HISTORIA

            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text="Motivo de la visita", width=30, font=("Verdana", 15,"bold"), background="palegreen")
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=3)

            self.lblOperacionEditar = tk.Label(self.frameEditarHistoria, text="Operación", width=30, font=("Verdana", 15,"bold"), background="palegreen")
            self.lblOperacionEditar.grid(row=2, column=0, padx=5, pady=3)

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text="Tratamiento", width=30, font=("Verdana", 15,"bold"), background="palegreen")
            self.lblTratamientoEditar.grid(row=4, column=0, padx=5, pady=3)

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text="Detalle adicional", width=30, font=("Verdana", 15,"bold"), background="palegreen")
            self.lblDetalleEditar.grid(row=6, column=0, padx=5, pady=3)

            #ENTRYS EDITAR HISTORIA

            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=("Verdana", 15))
            self.entryMotivoEditar.grid(row = 1, column=0, pady=3, padx=5, columnspan=2)

            self.svOperacionEditar = tk.StringVar()
            self.entryOperacionEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svOperacionEditar)
            self.entryOperacionEditar.config(width=65, font=("Verdana", 15))
            self.entryOperacionEditar.grid(row = 3, column=0, pady=3, padx=5, columnspan=2)

            self.svTratamientoEditar = tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=65, font=("Verdana", 15))
            self.entryTratamientoEditar.grid(row = 5, column=0, pady=3, padx=5, columnspan=2)

            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=65, font=("Verdana", 15))
            self.entryDetalleEditar.grid(row = 7, column=0, pady=3, padx=5, columnspan=2)

            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(background="palegreen")
            self.frameFechaEditar.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
                
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text="Fecha y Hora", width=30, font=("Verdana", 15,"bold"), background="palegreen")
            self.lblFechaHistoriaEditar.grid(row=0, column=0, padx=5, pady=3)

            #  ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=("Verdana", 15))
            self.entryFechaHistoriaEditar.grid(row = 0, column=1, pady=3, padx=5)

            #INSERTAR LOS VALORES A LOS ENTRYS

            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar) # 0 es la locación
            self.entryOperacionEditar.insert(0, self.operacionHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            #BUTTON EDITAR HISTORIA
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text="Editar Historia", command = self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=("Verdana", 12,"bold"), foreground="snow", background="royalblue2", cursor="hand2", activebackground="royalblue4")
            self.btnEditarHistoriaMedica.grid(row=1, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text="Salir", command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20, font=("Verdana", 12,"bold"), foreground="gray99", background="gray25", cursor="hand2", activebackground="gray2")
            self.btnSalirEditarHistoriaMedica.grid(row=1, column=1, padx=10, pady=5)

            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica

            self.idHistoriaMedica = None

        except:
            titulo = "Editar Historia"
            mensaje = "Error al editar historia"
            messagebox.showerror(titulo, mensaje)

    def historiaMedicaEditar(self):

        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svOperacionEditar.get(), self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.historiaMedica()
            
        except:
            titulo = "Editar Historia"
            mensaje = "Error al editar historia"
            messagebox.showerror(titulo, mensaje)
            self.topEditarHistoria.destroy()

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

    AppError.mainloop()