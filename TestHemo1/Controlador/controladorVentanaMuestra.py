from PyQt4.QtCore import QString

__author__ = 'Sapo'
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery


class ControladorVentanaMuestra():

    def __init__(self):
        self.idMuestra = 0

    def conectar(self):
        self.db1 = QSqlDatabase.addDatabase("QMYSQL")
        self.db1.setHostName("localhost")
        self.db1.setDatabaseName("hemodb")
        self.db1.setUserName("root")
        self.db1.setPassword("hemo")
        self.db1.open()

    def entregarDatos(self,select):
        self.conectar()
        projectModel = QSqlQueryModel()
        if select== 'todos':
            projectModel.setQuery("select m.codigoFrasco as Frasco, p.nombre as Nombre, p.dni as DNI,p.apellido as Apellido, m.fechaIngreso as Ingreso, m.fechaEgreso as Egreso,m.idmuestra as Numero, m.estado as Estado, o.apellido as Operario, m.comentario as Comentario from  muestra m inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario  ",self)
        if select== 'negativo':
            projectModel.setQuery("select m.codigoFrasco as Frasco, p.nombre as Nombre, p.dni as DNI,p.apellido as Apellido, m.fechaIngreso as Ingreso, m.fechaEgreso as Egreso,m.idmuestra as Numero, m.estado as Estado, o.apellido as Operario, m.comentario as Comentario from  muestra m inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario where m.estado = 4 ",self)
        if select== 'positivo':
            projectModel.setQuery("select m.codigoFrasco as Frasco, p.nombre as Nombre, p.dni as DNI,p.apellido as Apellido, m.fechaIngreso as Ingreso, m.fechaEgreso as Egreso,m.idmuestra as Numero , m.estado as Estado, o.apellido as Operario, m.comentario as Comentario from  muestra m inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario where m.estado = 3 ",self)
        if select== 'abortado':
            projectModel.setQuery("select m.codigoFrasco as Frasco, p.nombre as Nombre, p.dni as DNI,p.apellido as Apellido, m.fechaIngreso as Ingreso, m.fechaEgreso as Egreso,m.idmuestra as Numero , m.estado as Estado, o.apellido as Operario, m.comentario as Comentario from  muestra m inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario where m.estado = 1 ",self)
        self.db1.close()
        return projectModel

    def busqueda(self,datoAbuscar, estado, fechaInicio, fechaFin):
        self.conectar()
        projectModel = QSqlQueryModel()
        if fechaInicio != "fecha inicio":
            desde = " and '"+ fechaInicio + "' <= fechaEgreso"
            if fechaFin != 'fecha fin    ':
                desde +=  " and '"
        if fechaFin != 'fecha fin    ':
            hasta = fechaFin + "' >= m.fechaEgreso"
            if fechaInicio == "fecha inicio":
                hasta = " and '"  + fechaFin +"' <= "
        if fechaInicio == "fecha inicio":
            desde= ""
        if fechaFin == 'fecha fin    ':
            hasta = ""
        if fechaInicio != "fecha inicio" and fechaFin != 'fecha fin    ':
            desde = " and fechaEgreso between '"+fechaInicio+"' and '"+fechaFin+"'"
            hasta = ""
        if estado == "positivo":
            cadena = "where estado= 3 and "
        if estado == "negativo":
            cadena = "where estado = 4 and "
        if estado == "abortado":
            cadena = "where estado = 1 and "
        if estado == "todos":
            cadena ="where "
        query ="select m.codigoFrasco as Frasco, p.nombre as Nombre, p.apellido as Apellido,p.dni as DNI, m.fechaIngreso as Ingreso, m.fechaEgreso as Egreso,m.idmuestra as Numero,  m.resultado as Resultado, o.apellido as Operario, m.comentario as Comentario from  muestra m inner join paciente p on m.paciente_idpaciente1 = p.idpaciente inner join operario o on m.operario_idoperario1 = o.idoperario "+cadena+  " p.dni like " + "\'" + datoAbuscar+ "%" + "\'" + desde + hasta + " and not (m.fechaEgreso is null)"

        projectModel.setQuery(query)
        self.db1.close()
        return projectModel

    def busquedaPaciente(self,datoAbuscar):
        self.conectar()
        projectModel = QSqlQueryModel()
        query ="select nombre, apellido, dni, codigo from paciente where dni like " + "\'" + datoAbuscar+ "%" + "\'"
        projectModel.setQuery(query)
        self.db1.close()
        return projectModel

    def actualizarPaciente(self,dato, idmuestra):
        self.conectar()
        projectModel = QSqlQuery()
        projectModel1 =QSqlQuery()
        projectModel.exec_("select idpaciente from paciente where dni = " + dato)
        while projectModel.next():
            a = QString
            a = projectModel.value(0).toString()
        projectModel1.exec_("update muestra set paciente_idpaciente1= " + a +" where idmuestra = " + idmuestra)
        self.db1.close()
