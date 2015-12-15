import MySQLdb
from PyQt4.QtGui import QMessageBox
from ConexionDB.conexiondb import DBConn

__author__ = 'ale'



class Usuario:
    def __init__(self):
        self.id = 0
        self.codigo = 123
        self.nombre = ''
        self.apellido = ''
        self.username = ''
        self.password = ''
        self.db = DBConn()


    def nuevo(self):
        #Crear un nuevo usuario


        query = "INSERT INTO operario (codigo, nombre, apellido, username, password) VALUES ( %s, %s, %s, %s, %s )"
        values = (self.codigo, self.nombre, self.apellido, self.username, self.password)
        self.db.insertar(query,values)

        mb = QMessageBox()
        mb.setText('usuario guardado')
        mb.exec_()

