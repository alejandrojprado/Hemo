__author__ = 'ale'

import random
from ConexionDB.conexiondb import DBConn
import datetime
import time




class ControladorVentanaPrincipal:

    def __init__(self):
            self.db = DBConn()

    def passUsuario(self, nombre):
        query = """select password from operario where username = %s """
        valor = (nombre)
        passw = self.db.consulta(query, valor)
        if passw == None:
            retur = False
        else:
            return passw[0]


    def estadoAceptado(self, idmuestra):
        if idmuestra != None:
            query = "select fechaResultadoAC from muestra where idmuestra = %s"
            valor= self.db.consulta(query,idmuestra)
            if valor == None:
                return False
            else:
                return True
        else:
            return True

    def cambiar(self):
        img  = {4 :'cVerde', 0 :'cGris' , 3 :'cRojo', 1 : 'cAmarillo'}
        query = """select estado, tiempoActual_min,  alarma, horaOcupacion, muestra_idmuestra from celda limit 20"""
        t = self.db.consultaMuchos(query)
        list(t)
        datos= []
        celda = 0
        for i in t:
            color = i[0]
            color = img[color]
            horas = 0
            if i[1] != None:
                segundos = i[1]*60
                dias=str(datetime.timedelta(seconds=segundos).days) + "d "
                horas= "Trascurrido:\n"+dias + time.strftime ("%Hh %Mm", time.gmtime(segundos))
            if i[2] > 0 and i[2] < 3:
                alarma = 1
            else:
                alarma = 0
            fechaIngreso = "                           "
            celda = celda +1
            if i[3] != None:
                fechaIngreso = "Ingreso:\n"+i[3].strftime("%d/%m/%Y   ")
            datos.append([color,fechaIngreso,  horas,alarma, celda, i[4]])
        return datos

    def temperatura(self):
        query = "select tempActual from temperatura"
        return self.db.consulta(query)
