from Conexion.conexion import ConexionDB
from tkinter import messagebox

################### CLASE HistoriaMedica ################################

class Operaciones:
    """Clase de la tabla Operaciones"""

    def __init__(self, Operacion2, Precio2):
        """Constructor cuyos parámetros son los nombres de las columnas de la Tabla Operaciones"""

        self.Operacion2 = Operacion2
        self.Precio2=Precio2
    
    def __str__(self):
        """Método que muestra los objetos"""

        return f"Operaciones[{self.Operacion2},{self.Precio2}]"

##################### FUNCIONES QUE VINCULAN A SQLITE ########################################

#:::::::::::::::::::::::::::::: GUARDAR HISTORIA ::::::::::::::::::::::::::::::::::::

def guardarOperaciones(Operacion2, Precio2):
    """Función que guarda los datos en la clase Operaciones"""

    conexion = ConexionDB()
    sql = f"""INSERT INTO Operaciones (Operacion2, Precio2) VALUES
            ("{Operacion2}","{Precio2}")"""

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

def eliminarOperaciones(id):
    """Función que elimina permanentemente los datos en la clase Operaciones"""

    conexion = ConexionDB()
    sql = f"DELETE FROM Operaciones WHERE id = {id}"

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
    
    sql = f"SELECT Operacion2 FROM Operaciones WHERE TRUE"
    
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
    
    sql = f"SELECT Precio2 FROM Operaciones WHERE TRUE"
   
    try:
        conexion.cursor.execute(sql)
        listaPrecio = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar precio"
        messagebox.showerror(titulo, mensaje)

    return listaPrecio