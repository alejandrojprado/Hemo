__author__ = 'ale'
from ConexionDB.conexiondb import DBConn
class ControladorVentanitaAlarma:

    def __init__(self):
        self.db = DBConn()

    def updateAC(self, celda):
        queryselect ="""select muestra_idmuestra from celda where numero = %s"""
        idmuestra = self.db.consulta(queryselect,celda)[0]
        if idmuestra != None:
            query1 = """select fechaResultadoAC from muestra where idmuestra = %s"""
            resultado = self.db.consulta(query1, idmuestra)[0]
            if resultado == None:
                query = """update muestra set fechaResultadoAC = now()  where idmuestra = %s"""
                self.db.actualizar(query,idmuestra)

    def consultas(self, celda):
        queryselect ="""select muestra_idmuestra from celda where numero = %s"""
        idmuestra = self.db.consulta(queryselect,celda)[0]
        if idmuestra != None:
            query1 = """select fechaResultado from muestra where idmuestra = %s"""
            resultado = self.db.consulta(query1, idmuestra)[0]
            if resultado == None:
                query = """update muestra set fechaResultado = now()  where idmuestra = %s"""
                self.db.actualizar(query,idmuestra)
                resultado = self.db.consulta(query1, idmuestra)[0]
            return resultado
