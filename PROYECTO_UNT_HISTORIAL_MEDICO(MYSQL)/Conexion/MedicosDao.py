from Conexion.conexion import ConexionDB
from tkinter import messagebox

##################### FUNCIONES QUE VINCULAN A MYSQL ########################################

def activarLinea(idMedico):
    """Función que activa la linea de un medico"""
    
    conexion = ConexionDB()
    sql = f"""UPDATE Medicos SET Linea = 1 WHERE idMedico = {idMedico}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()

    except:
        titulo = "ERROR"
        mensaje = "Error al activar línea del médico"
        messagebox.showinfo(titulo, mensaje)    
        
def desactivarLinea(idMedico):
    """Función que desactiva la linea de un medico"""
    
    conexion = ConexionDB()
    sql = f"""UPDATE Medicos SET Linea = 0 WHERE idMedico = {idMedico}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()

    except:
        titulo = "ERROR"
        mensaje = "Error al desactivar línea del médico"
        messagebox.showinfo(titulo, mensaje)    

def seleccionarActivo():
    """Función que selecciona el nombre del medico activo"""
    conexion = ConexionDB()
    MedicoActivo = []
    
    sql = f"SELECT NombreMedico FROM Medicos WHERE Linea = 1"
    
    try:
        conexion.cursor.execute(sql)
        MedicoActivo = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()  
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar MedicoActivo"
        messagebox.showerror(titulo, mensaje) 
           
    return MedicoActivo

def seleccionarInactivo():
    """Función que selecciona el nombre de los medicos inactivos"""
    conexion = ConexionDB()
    MedicoInactivo = []
    
    sql = f"SELECT NombreMedico FROM Medicos WHERE Linea = 0"
    
    try:
        conexion.cursor.execute(sql)
        MedicoInactivo = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()  
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar MedicoInactivo"
        messagebox.showerror(titulo, mensaje) 
           
    return MedicoInactivo

def seleccionarIDActivo():
    """Función que selecciona el id del medico activo"""
    conexion = ConexionDB()
    MedicoIDActivo = []
    
    sql = f"SELECT idMedico FROM Medicos WHERE Linea = 1"
    
    try:
        conexion.cursor.execute(sql)
        MedicoIDActivo = list(conexion.cursor.fetchall())
        conexion.cerrarConexion()  
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar MedicoActivo"
        messagebox.showerror(titulo, mensaje) 
           
    return MedicoIDActivo

