from PyQt4.QtGui import QMessageBox
from ConexionDB.conexiondb import DBConn

class ControladorVentanaHemocultivo():
    def __init__(self):
        self.db = DBConn()

    def cancelar(self):
        query =("""delete from muestra where altaHabilitada = 1""")
        self.db.actualizar(query)

    def insertar(self, datosPaciente, codScan, operario):

        query = ("""INSERT INTO paciente(codigo, nombre, apellido, dni) VALUES (%s,%s,%s, %s)""")
        valor = datosPaciente
        self.db.insertar(query, valor)
        query1 = ("""select idpaciente  from paciente where dni = %s """)
        valor1 = datosPaciente[3]
        idpaciente = self.db.consulta(query1, valor1)[0]


        query2 = ("""select idoperario  from operario where username = %s """)
        valor2 = operario

        idoperario = self.db.consulta(query2, valor2)[0]



        query3 = ("""INSERT INTO muestra(operario_idoperario1, paciente_idpaciente1, tiempoAnalisis, tiempoActual, resultado, estado, colorFrascoIngreso,
         colorFrascoEgreso, fechaIngreso, fechaEgreso, fechaResultado, fechaResultadoAC, codigoFrasco, numeroCelda, altaHabilitada) VALUES (%s,%s,7200, 0, null, 1, null,null, now(),null, null, null, %s, 0, 1)""")
        valor3 = (idoperario, idpaciente, codScan)
        self.db.insertar(query3, valor3)

        query4 = ("""select idmuestra  from muestra where codigoFrasco = %s """)
        valor4 = codScan
        idmuestra = self.db.consulta(query4, valor4)[0]
        return idmuestra

    def control(self, idmuestra):
        query1 = ("""select altaHabilitada  from muestra where idmuestra = %s """)
        valormuestra = idmuestra
        a = self.db.consulta(query1, valormuestra)[0]

        return a




    def controlExistencia(self, codigo, ventana):

        query = ("select * from muestra where codigoFrasco = %s")
        valor = codigo
        if self.db.consulta(query,valor) == None:
            return True
        else:
            self.mensajedeerror(ventana,mensaje =  "Codigo repetido")
            return  False


    def mensajedeerror(self, cosa, mensaje="error al completar los datos"):
        QMessageBox.warning(cosa,"error", mensaje, QMessageBox.Ok)

