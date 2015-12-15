__author__ = 'ale'

import MySQLdb
class DBConn:

    def __init__(self, db_host= 'localhost' ,db_port=3306, db_user='root', db_pass='hemo', db_name='hemodb'):
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    def conectar(self):
        return MySQLdb.connect(host=self.db_host, port = self.db_port, user=self.db_user, passwd=self.db_pass, db=self.db_name)


    def insertar(self, query, valor = ''):      # insert
        db = self.conectar()
        cursor = db.cursor()
        cursor.execute(query, valor)
        db.commit()
        cursor.close()

    def consulta(self, query, valor= ""):   # traer datos (select)
        db = self.conectar()
        cursor = db.cursor()
        if valor != "":                                                    # con where
           cursor.execute(query, valor)
        else:                                                                     # sin where
            cursor.execute(query)
        dato = cursor.fetchone()
        cursor.close()
        return dato

    def consultaMuchos(self, query, valor= ""):   # traer datos (select)
        db = self.conectar()
        cursor = db.cursor()
        if valor != "":                                                    # con where
           cursor.execute(query, valor)
        else:                                                                     # sin where
            cursor.execute(query)
        dato = cursor.fetchall()
        cursor.close()
        return dato

    def actualizar(self, query, valor=""):                        # update
        db = self.conectar()
        cursor = db.cursor()
        if valor != "":                                                    # con where
           cursor.execute(query, valor)
        else:                                                                     # sin where
            cursor.execute(query)
        db.commit()
        cursor.close()


    def actualizar2(self, query, valor=""):                        # update
        db = self.conectar()
        cursor = db.cursor()
        if valor != "":                                                    # con where
           cursor.execute(query, valor)
        else:                                                                     # sin where
            cursor.execute(query)
        db.commit()
        cursor.close()



