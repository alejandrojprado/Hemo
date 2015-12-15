__author__ = 'ale'
from ConexionDB.conexiondb import DBConn
import time,datetime


class ControladorVentanaCelda():

    def __init__(self):
        self.idcelda = 0
        self.idmuestra = 0
        self.db = DBConn()


    def valoresGrafico(self, celda ):

        query = """select desvioTonalidadInicial, ultimaActualizacion from estadoceldalog where celda_idcelda = %s """
        datos =self.db.consultaMuchos(query, celda)

        s = []
        t = []
        for record in datos:
            t.append(record[0])
            s.append(record[1])
        return [s,t]

    def valoresTablasCelda(self, celda):
        query ="""select p.nombre , p.apellido,p.dni,p.codigo,  m.fechaIngreso,c.estado, m.tiempoAnalisis, c.tiempoActual_min,   m.codigoFrasco,  o.apellido , m.comentario, m.fechaResultado  from  celda c inner join muestra m on c.muestra_idmuestra = m.idmuestra  inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario where c.numero = %s """
        values = celda
        datos = self.db.consulta(query, values)
        if datos != None:
            datos= list(datos)
            datos[4]= datos[4].strftime("%d/%m/%Y %H:%M")
            segundos = datos[7]*60
            horas= time.strftime ("%H horas %M minutos", time.gmtime(segundos))
            dias=str(datetime.timedelta(seconds=segundos).days) + " dias "
            datos[7]=  dias +horas
            diccionario  = {1:"Analizando" , 3:"Positivo", 4:"Negativo"}
            datos[5]= diccionario[datos[5]]
            if datos[10] == None:
                datos[10]="No hay obsevaciones"
            if datos[11]!= None:

                dato12=datetime.datetime.now()
                dato12 = dato12.replace(microsecond=0) - datos[11]
                dato12= "%d dias %s horas %s minutos " % (dato12.days, (dato12.seconds/60)/60, (dato12.seconds/60)%60)


                datos[11]= datos[11].strftime("%d/%m/%Y %H:%M")

                datos.append(dato12)

        return datos

    def habilitarBaja(self, celda, codScan):
        query3= "select codigoFrasco from muestra where idmuestra = %s"
        codigoMuestra = self.db.consulta(query3, self.idmuestra)[0]
        if int(codigoMuestra) == int(codScan) :

            return True
        else:
            return False

    def retirar(self, celda):
            resultados={1:"'Abortado'", 3:"'Positivo'", 4:"'Negativo'"}
            query = """select estado,idcelda from celda where numero = %s"""
            datos = self.db.consulta(query, celda)
            estado = datos[0]
            idcelda = datos[1]
            resultado = resultados[estado]
            query2 = """update muestra set fechaEgreso = now(),  resultado = """+resultado+ """, estado = """+str(estado)+""" where idmuestra = %s"""
            self.db.actualizar2(query2, self.idmuestra)
            query = """update celda set muestra_idmuestra = null, estado =0 where numero = %s"""
            valor = celda
            self.db.actualizar(query, valor)
            query3= """update estadocelda set ocupada = 0, estado = 0, horaOcupacion = null, tiempoActual_min = null where celda_idcelda = %s"""
            self.db.actualizar(query3, idcelda)

    def controlRetirar(self, celda):
        query1 = ("""select bajaHabilitada, alarma  from celda where numero = %s """)
        valor = self.db.consulta(query1, celda)
        alarma = valor[1]
        if alarma == 2:
            query3="update celda set bajaHabilitada = 0 where bajaHabilitada=1"
            self.db.actualizar(query3)
        return valor[0]

    def extender(self, tiempo, celda):
        queru1 = """select muestra_idmuestra from celda where numero = %s"""
        valor = self.db.consulta(queru1, celda)
        tiempo = tiempo*1440
        query = "update muestra set tiempoAnalisis = " + str(tiempo) + " where idmuestra = %s"
        self.db.actualizar(query,valor)

    def cancelar(self):
        query2 = """update muestra set fechaEgreso = null, estado = null,  resultado = null where idmuestra = %s"""
        self.db.actualizar(query2, self.idmuestra)
        query = """update celda set bajaHabilitada=0 where bajaHabilitada=1"""
        self.db.actualizar(query)

    def obtenerIdCelda(self,celda):
        query= """select idcelda, muestra_idmuestra, estado from celda where numero = %s"""
        valor =  self.db.consulta(query,celda)
        self.idcelda = valor[0]
        self.idmuestra = valor[1]
        return valor
