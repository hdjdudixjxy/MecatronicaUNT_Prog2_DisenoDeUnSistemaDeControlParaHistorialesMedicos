from Conexion.conexion import ConexionDB
from tkinter import messagebox

class Login:
    """Clase de la tabla Login"""

    def __init__(self, Trabajador, Usuario, Contrasena):
        """Constructor cuyos parámetros son los nombres de las columnas de la Tabla Operaciones"""

        self.Trabajador = Trabajador
        self.Usuario = Usuario
        self.Contrasena = Contrasena
    
    def __str__(self):
        """Método que muestra los objetos"""

        return f"Login[{self.Trabajador},{self.Usuario},{self.Contrasena}]"

##################### FUNCIONES QUE VINCULAN A SQLITE ########################################

#:::::::::::::::::::::::::::::: GUARDAR HISTORIA ::::::::::::::::::::::::::::::::::::

def guardarLogin(Trabajador, Usuario, Contrasena):
    """Función que guarda los datos en la clase Login"""

    conexion = ConexionDB()
    sql = f"""INSERT INTO Login (Trabajador, Usuario, Contrasena) VALUES
            ("{Trabajador}","{Usuario}","{Contrasena}")"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Registro Operación"
        mensaje = "Operación registrada exitosamente"
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = "Registro Operación"
        mensaje = "Error al registrar operación"
        messagebox.showerror(titulo, mensaje)

#::::::::::::::::::::::::: TREEVIEW EN LA GUI LOGIN :::::::::::::::::::::::::::::::::::::

def listarLogin():
    conexion = ConexionDB()
    listaLogin = []
    
    sql = f"SELECT * FROM Login WHERE TRUE"
    
    try:
        conexion.cursor.execute(sql)
        listaLogin = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar Login"
        messagebox.showerror(titulo, mensaje)

    return listaLogin

def listarCondicionLogin():
    """Función que crea una lista y hace que se genere una lista que contenga las contraseñas"""

    conexion = ConexionDB()
    listaCondicionLogin = []
    
    sql = f"""SELECT Contrasena FROM Login WHERE TRUE"""
    
    try:
        conexion.cursor.execute(sql)
        listaCondicionLogin = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar Login Condicion"
        messagebox.showerror(titulo, mensaje)

    return listaCondicionLogin

def listarCondicionLogin2():
    """Función que crea una lista y hace que se genere una lista que contenga los usuarios"""

    conexion = ConexionDB()
    listaCondicionLogin2 = []
    
    sql = f"""SELECT Usuario FROM Login WHERE TRUE"""
    
    try:
        conexion.cursor.execute(sql)
        listaCondicionLogin2 = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar Login Condicion"
        messagebox.showerror(titulo, mensaje)

    return listaCondicionLogin2