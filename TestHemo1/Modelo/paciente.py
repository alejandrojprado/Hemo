from ConexionDB.conexiondb import DBConn

__author__ = 'ale'
from PyQt4.QtGui import QMessageBox


class Usuario:
    def __init__(self):
        self.codigo = 123
        self.nombre = ''
        self.apellido = ''
        self.db = DBConn()

    def nuevo(self):
        #Crear un nuevo paciente
        query = "INSERT INTO operario (codigo, nombre, apellido) VALUES ( %s, %s, %s )"
        values = (self.codigo, self.nombre, self.apellido)
        self.db.ejecutar(query, values)
        mb = QMessageBox()
        mb.setText('usuario guardado')
        mb.exec_()
