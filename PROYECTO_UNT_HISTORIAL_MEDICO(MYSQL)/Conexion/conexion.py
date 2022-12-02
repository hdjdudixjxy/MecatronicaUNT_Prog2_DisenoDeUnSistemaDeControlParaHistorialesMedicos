import pymysql

class ConexionDB:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='bj6rut9nh6zecwktf8pe-mysql.services.clever-cloud.com',
            user='updoyj6wjsteofrk',
            password='zIu4diili79hRYm7dsU5',
            db='bj6rut9nh6zecwktf8pe'
            ) # nos conectamos a la base de datos
        self.cursor = self.conexion.cursor() # el metodo cursor nos permite modificar datos

    def cerrarConexion(self):
        self.conexion.commit() # subimos los datos insertados en los entrys
        self.conexion.close() # cerramos la conexión
        
