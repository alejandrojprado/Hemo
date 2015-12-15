__author__ = 'ale'
from ConexionDB.conexiondb import DBConn
class ControladorVentanaPaciente:

    def __init__(self):
        self.db = DBConn()

    def nuevoPaciente(self, datosPaciente):
        query = ("""INSERT INTO paciente( nombre, apellido, dni, codigo) VALUES (%s,%s,%s, %s)""")
        valor = datosPaciente
        self.db.insertar(query, valor)

