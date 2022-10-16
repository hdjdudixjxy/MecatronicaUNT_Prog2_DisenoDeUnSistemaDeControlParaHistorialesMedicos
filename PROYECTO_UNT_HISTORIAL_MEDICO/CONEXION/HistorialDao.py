from CONEXION.conexion import ConexionDB
from tkinter import messagebox

################### CLASE HistoriaMedica ################################

class HistoriaMedica:
    """Clase de la tabla HistoriaMedica"""

    def __init__(self, idPersona, FechaHistoria, MotivoDeLaVisita, Operacion, Tratamiento, DetalleAdicional, Precio):
        """Constructor cuyos parámetros son los nombres de las columnas de la Tabla HistoriaMedica"""

        self.idHistorial = None
        self.idPersona = idPersona
        self.FechaHistoria = FechaHistoria
        self.MotivoDeLaVisita = MotivoDeLaVisita
        self.Operacion = Operacion
        self.Tratamiento = Tratamiento
        self.DetalleAdicional = DetalleAdicional
        self.Precio=Precio
    
    def __str__(self):
        """Método que muestra los objetos"""

        return f"HistoriaMedica[{self.idPersona},{self.FechaHistoria},{self.MotivoDeLaVisita}, {self.Operacion}, {self.Tratamiento}, {self.DetalleAdicional},{self.Precio}]"

##################### FUNCIONES QUE VINCULAN A SQLITE ########################################

#:::::::::::::::::::::::::::::: GUARDAR HISTORIA ::::::::::::::::::::::::::::::::::::

def guardarHistoria(idPersona, FechaHistoria, MotivoDeLaVisita, Operacion, Tratamiento, DetalleAdicional, Precio):
    """Función que guarda los historiales en la clase HistoriaMedica"""

    conexion = ConexionDB()
    sql = f"""INSERT INTO HistoriaMedica (idPersona, FechaHistoria, MotivoDeLaVisita, Operacion, Tratamiento, DetalleAdicional, Precio) VALUES
            ({idPersona},"{FechaHistoria}","{MotivoDeLaVisita}","{Operacion}","{Tratamiento}","{DetalleAdicional}","{Precio}")"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Registro Historia Medica"
        mensaje = "Historia registrada exitosamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Registro Historia Medica"
        mensaje = "Error al registrar historia"
        messagebox.showerror(titulo, mensaje)

#::::::::::::::::::::::::::: ELIMINAR HISTORIA ::::::::::::::::::::::::::::::::::::

def eliminarHistoria(idHistorial):
    """Función que elimina permanentemente los historiales en la clase HistoriaMedica"""

    conexion = ConexionDB()
    sql = f"DELETE FROM HistoriaMedica WHERE idHistorial = {idHistorial}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Eliminar Historia"
        mensaje = "Historia medica eliminada exitosamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar Historia"
        mensaje = "Error al eliminar historia medica"
        messagebox.showerror(titulo, mensaje)

#:::::::::::::::::::::::::::: EDITAR HISTORIA ::::::::::::::::::::::::::::::::::::

def editarHistoria(fechaHistoria, MotivoDeLaVisita, Operacion, Tratamiento, DetalleAdicional, Precio, idHistorial):
    """Función que edita los historiales en la clase HistoriaMedica"""

    conexion = ConexionDB()
    sql = f"""UPDATE HistoriaMedica SET fechaHistoria = "{fechaHistoria}", MotivoDeLaVisita = "{MotivoDeLaVisita}", Operacion = "{Operacion}", Tratamiento = "{Tratamiento}", DetalleAdicional = "{DetalleAdicional}", Precio = "{Precio}" WHERE idHistorial = {idHistorial}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = "Editar Historia"
        mensaje = "Historia medica editada exitosamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Editar Historia"
        mensaje = "Error al editar historia medica"
        messagebox.showerror(titulo, mensaje)

#::::::::::::::::::::::::: TABLA EN LA GUI :::::::::::::::::::::::::::::::::::::

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    
    sql = f"SELECT H.idHistorial, D.NombreCompleto || ' ' || D.ApellidosCompletos AS Paciente, H.FechaHistoria, H.MotivoDeLaVisita, H.Operacion, H.Tratamiento, H.DetalleAdicional, H.Precio FROM HistoriaMedica H INNER JOIN DatosPaciente D ON D.idPersona = H.idPersona WHERE D.idPersona = {idPersona}"
    # Cuando se cumple el parámetro WHERE, se cumple el INNER JOIN

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        titulo = "LISTAR"
        mensaje = "Error al listar historia medica"
        messagebox.showerror(titulo, mensaje)

    return listaHistoria