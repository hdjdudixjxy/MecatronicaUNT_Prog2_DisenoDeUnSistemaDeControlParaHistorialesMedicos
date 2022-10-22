from CONEXION.conexion import ConexionDB
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
            ("{Trabajador}","{Usuario}",{Contrasena})"""

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
        listaLogin = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar historia medica"
        messagebox.showerror(titulo, mensaje)

    return listaLogin
