__author__ = 'ale'
from ConexionDB.conexiondb import DBConn

class ControladorVistaDatos():

    def __init__(self):
        self.db = DBConn()

    def traerDatos(self, muestra):

        query = """select p.nombre , p.apellido,p.dni,p.codigo,  m.fechaIngreso, m.fechaEgreso,m.fechaResultado,  m.resultado, m.tiempoAnalisis, m.codigoFrasco, o.apellido , m.comentario from  muestra m  inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario where m.idmuestra = %s """

        tupla = self.db.consulta(query,muestra)

        listadatos = list(tupla)
        desde = listadatos[4]
        hasta = listadatos[5]
        listadatos[4]= listadatos[4].strftime("%d/%m/%Y %H:%M")
        listadatos[5]= listadatos[5].strftime("%d/%m/%Y %H:%M")
        if listadatos[6]!= None:
            listadatos[6]= listadatos[6].strftime("%d/%m/%Y %H:%M")
        if listadatos[11] == None:
            listadatos[11]="No hay obsevaciones"
        listadatos[8] = hasta - desde

        return listadatos

    def valoresGrafico(self, muestra ):
        query = """select desvio, fecha from graficomuestra  where muestra_idmuestra= %s """
        values=(muestra)
        datos =self.db.consultaMuchos(query, values)
        t = []
        s = []
        for record in datos:
                t.append(record[0])
                s.append(record[1])
        return [s,t]

    def datosCombo(self):
        listaNombres = {}
        query= """ select nombre, apellido, idpaciente from paciente"""
        for i in self.db.consultaMuchos(query):
            if i[0] != "Anonimo":
                listaNombres[ i[0] +" "+i [1]] =int( i[2])
        return listaNombres

    def asignar(self, idpaciente, muestra):
        if idpaciente != 0:
            idpaciente= str(idpaciente)
            query= "update muestra set paciente_idpaciente1 = "+idpaciente + " where idmuestra = %s"
            self.db.actualizar(query, muestra)