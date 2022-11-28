import pymysql

class ConexionDB:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='J30*l4c1V10',
            db='classicmodels'
            ) # nos conectamos a la base de datos
        self.cursor = self.conexion.cursor() # el metodo cursor nos permite modificar datos

    def cerrarConexion(self):
        self.conexion.commit() # subimos los datos insertados en los entrys
        self.conexion.close() # cerramos la conexión