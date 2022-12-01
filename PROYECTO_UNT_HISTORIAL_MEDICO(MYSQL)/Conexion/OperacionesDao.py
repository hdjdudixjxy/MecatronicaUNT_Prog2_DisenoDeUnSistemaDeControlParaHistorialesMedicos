from Conexion.conexion import ConexionDB
from tkinter import messagebox

################### CLASE HistoriaMedica ################################

class Operaciones:
    """Clase de la tabla Operaciones"""

    def __init__(self, Tipo, Precio):
        """Constructor cuyos parámetros son los nombres de las columnas de la Tabla Operaciones"""

        self.Tipo = Tipo
        self.Precio=Precio
    
    def __str__(self):
        """Método que muestra los objetos"""

        return f"Operaciones[{self.Tipo},{self.Precio}]"

##################### FUNCIONES QUE VINCULAN A SQLITE ########################################

#:::::::::::::::::::::::::::::: GUARDAR HISTORIA ::::::::::::::::::::::::::::::::::::

def guardarOperaciones(Tipo, Precio):
    """Función que guarda los datos en la clase Operaciones"""

    conexion = ConexionDB()
    sql = f"""INSERT INTO Operaciones (Tipo, Precio) VALUES
            ("{Tipo}","{Precio}")"""

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

#::::::::::::::::::::::::::: ELIMINAR HISTORIA ::::::::::::::::::::::::::::::::::::

def eliminarOperaciones(idOperacion):
    """Función que elimina permanentemente los datos en la clase Operaciones"""

    conexion = ConexionDB()
    sql = f"DELETE FROM Operaciones WHERE idOperacion = {idOperacion}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Eliminar operación"
        mensaje = "Operación eliminada exitosamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar operación"
        mensaje = "Error al eliminar operación"
        messagebox.showerror(titulo, mensaje)

#::::::::::::::::::::::::: LISTBOX EN LA GUI :::::::::::::::::::::::::::::::::::::

def listarOperacion():
    conexion = ConexionDB()
    listaOperacion = []
    
    sql = f"SELECT Tipo FROM Operaciones WHERE TRUE"
    
    try:
        conexion.cursor.execute(sql)
        listaOperacion = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()

    except:
        titulo = "LISTAR"
        mensaje = "Error al listar operacion"
        messagebox.showerror(titulo, mensaje)

    return listaOperacion

def listarPrecio():
    conexion = ConexionDB()
    listaPrecio = []
    
    sql = f"SELECT Precio FROM Operaciones WHERE TRUE"
   
    try:
        conexion.cursor.execute(sql)
        listaPrecio = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar precio"
        messagebox.showerror(titulo, mensaje)

    return listaPrecio