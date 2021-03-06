from time import sleep

__author__ = 'ale'

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaHemocultivo.ui'
#
# Created: Sat Aug  1 11:41:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QInputDialog, QMessageBox
from Controlador.controladorventanahemocultivo import ControladorVentanaHemocultivo
from Aux.validador import validador

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class VentanaHemocultivo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.validador = validador()
        self.setupUi(self)
        self.setWindowTitle('Nueva Muestra')

    def setupUi(self, FormnHemocultivo):

        FormnHemocultivo.setObjectName(_fromUtf8("FormnHemocultivo"))


        FormnHemocultivo.setWindowModality(QtCore.Qt.ApplicationModal)
        FormnHemocultivo.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        FormnHemocultivo.resize(800, 600)
        self.centralwidget = QtGui.QWidget(FormnHemocultivo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 26, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.GpacienteDatos = QtGui.QGroupBox(self.groupBox)
        self.GpacienteDatos.setObjectName(_fromUtf8("GpacienteDatos"))
        self.GpacienteDatos.show()
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.GpacienteDatos)
        self.verticalLayout_2.setContentsMargins(-1, 24, 65, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pacienteNombre = QtGui.QLabel(self.GpacienteDatos)
        self.pacienteNombre.setObjectName(_fromUtf8("pacienteNombre"))
        self.verticalLayout_2.addWidget(self.pacienteNombre)
        self.lineNombre = QtGui.QLineEdit(self.GpacienteDatos)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.verticalLayout_2.addWidget(self.lineNombre)
        self.pacienteApellido = QtGui.QLabel(self.GpacienteDatos)
        self.pacienteApellido.setObjectName(_fromUtf8("pacienteApellido"))
        self.verticalLayout_2.addWidget(self.pacienteApellido)
        self.lineApellido = QtGui.QLineEdit(self.GpacienteDatos)
        self.lineApellido.setObjectName(_fromUtf8("lineApellido"))
        self.verticalLayout_2.addWidget(self.lineApellido)
        self.pacienteDNI = QtGui.QLabel(self.GpacienteDatos)
        self.pacienteDNI.setObjectName(_fromUtf8("pacienteDNI"))
        self.verticalLayout_2.addWidget(self.pacienteDNI)
        self.lineDNI = QtGui.QLineEdit(self.GpacienteDatos)
        self.lineDNI.setObjectName(_fromUtf8("lineDNI"))
        self.verticalLayout_2.addWidget(self.lineDNI)
        self.pacienteCodInterno = QtGui.QLabel(self.GpacienteDatos)
        self.pacienteCodInterno.setObjectName(_fromUtf8("pacienteCodInterno"))
        self.verticalLayout_2.addWidget(self.pacienteCodInterno)
        self.lineOC = QtGui.QLineEdit(self.GpacienteDatos)
        self.lineOC.setObjectName(_fromUtf8("lineOC"))
        self.verticalLayout_2.addWidget(self.lineOC)
        self.verticalLayout.addWidget(self.GpacienteDatos)
        self.GBfrascos = QtGui.QGroupBox(self.groupBox)
        self.GBfrascos.setTitle(_fromUtf8(""))
        self.GBfrascos.setObjectName(_fromUtf8("GBfrascos"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.GBfrascos)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.GBfrascos)
        self.groupBox_3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Bfrasco1 = QtGui.QPushButton(self.groupBox_3)
        self.Bfrasco1.setMinimumSize(QtCore.QSize(0, 52))
        self.Bfrasco1.setObjectName(_fromUtf8("Bfrasco1"))
        self.horizontalLayout_2.addWidget(self.Bfrasco1)
        self.Bfrasco2 = QtGui.QPushButton(self.groupBox_3)
        self.Bfrasco2.setMinimumSize(QtCore.QSize(0, 52))
        self.Bfrasco2.setObjectName(_fromUtf8("Bfrasco2"))
        self.horizontalLayout_2.addWidget(self.Bfrasco2)
        self.Bfrasco3 = QtGui.QPushButton(self.groupBox_3)
        self.Bfrasco3.setMinimumSize(QtCore.QSize(0, 52))
        self.Bfrasco3.setObjectName(_fromUtf8("Bfrasco3"))
        self.horizontalLayout_2.addWidget(self.Bfrasco3)
        self.Bfrasco4 = QtGui.QPushButton(self.groupBox_3)
        self.Bfrasco4.setMinimumSize(QtCore.QSize(0, 52))
        self.Bfrasco4.setObjectName(_fromUtf8("Bfrasco4"))
        self.horizontalLayout_2.addWidget(self.Bfrasco4)
        self.Bfrasco5 = QtGui.QPushButton(self.groupBox_3)
        self.Bfrasco5.setMinimumSize(QtCore.QSize(0, 52))
        self.Bfrasco5.setObjectName(_fromUtf8("Bfrasco5"))
        self.horizontalLayout_2.addWidget(self.Bfrasco5)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.GBfrascos)
        self.GBcancelar = QtGui.QGroupBox(self.groupBox)
        self.GBcancelar.setTitle(_fromUtf8(""))
        self.GBcancelar.setObjectName(_fromUtf8("GBcancelar"))
        self.Bcancelar = QtGui.QPushButton(self.GBcancelar)
        self.Bcancelar.setGeometry(QtCore.QRect(20, 50, 730, 27))
        self.Bcancelar.setObjectName(_fromUtf8("Bcancelar"))
        self.verticalLayout.addWidget(self.GBcancelar)
        self.horizontalLayout.addWidget(self.groupBox)
        FormnHemocultivo.setCentralWidget(self.centralwidget)
        self.retranslateUi(FormnHemocultivo)
        self.Bcancelar2 = QtGui.QPushButton(self)
        self.Bcancelar2.setGeometry(260, 500, 300, 30)
        self.Bcancelar2.setObjectName(_fromUtf8("Bcancelar2"))
        self.Bcancelar2.setText("Cancelar carga")
        self.Bcancelar2.hide()
        self.labelCarga = QtGui.QLabel(self)
        self.labelCarga.setGeometry(310, 330, 700, 30)
        self.labelCarga.setObjectName(_fromUtf8("labelCarga"))
        self.labelCarga.setText("Comprobando carga de la muestra")
        self.labelCarga.hide()
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(50, 250, 700, 50)
        self.progressBar.hide()
        self.checkBox.isChecked()
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accionCheck)
        QtCore.QObject.connect(self.Bcancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.Bcancelar2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancelar)
        QtCore.QMetaObject.connectSlotsByName(FormnHemocultivo)

    def retranslateUi(self, FormnHemocultivo):
        FormnHemocultivo.setWindowTitle(_translate("FormnHemocultivo", "MainWindow", None))
        self.groupBox.setTitle(_translate("FormnHemocultivo", "Nuevo Hemocultivo", None))
        self.checkBox.setText(_translate("FormnHemocultivo", "Anonimo", None))
        self.GpacienteDatos.setTitle(_translate("FormnHemocultivo", "Datos de paciente", None))
        self.pacienteNombre.setText(_translate("FormnHemocultivo", "Nombre", None))
        self.pacienteApellido.setText(_translate("FormnHemocultivo", "Apellido", None))
        self.pacienteDNI.setText(_translate("FormnHemocultivo", "DU/DNI", None))
        self.pacienteCodInterno.setText(_translate("FormnHemocultivo", "Otro codigo", None))
        self.groupBox_3.setTitle(_translate("FormnHemocultivo", "Seleccione cantidad de muestras a ingresar del paciente", None))
        self.Bfrasco1.setText(_translate("FormnHemocultivo", "1", None))
        self.Bfrasco2.setText(_translate("FormnHemocultivo", "2", None))
        self.Bfrasco3.setText(_translate("FormnHemocultivo", "3", None))
        self.Bfrasco4.setText(_translate("FormnHemocultivo", "4", None))
        self.Bfrasco5.setText(_translate("FormnHemocultivo", "5", None))
        self.Bcancelar.setText(_translate("FormnHemocultivo", "Cancelar", None))


    def cancelar(self):
        cvh = ControladorVentanaHemocultivo()
        cvh.cancelar()
        self.close()

    def accionCheck(self):
        if self.checkBox.isChecked():
            self.GpacienteDatos.setEnabled(False)
        else:
            self.GpacienteDatos.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_Bfrasco1_clicked(self):
        self.aceptando(1)

    @QtCore.pyqtSlot()
    def on_Bfrasco2_clicked(self):
        self.aceptando(2)

    @QtCore.pyqtSlot()
    def on_Bfrasco3_clicked(self):
        self.aceptando(3)

    @QtCore.pyqtSlot()
    def on_Bfrasco4_clicked(self):
        self.aceptando(4)

    @QtCore.pyqtSlot()
    def on_Bfrasco5_clicked(self):
        self.aceptando(5)

    def aceptando(self, veces):

        cvh = ControladorVentanaHemocultivo()
        datosUsuario = self.obtenerDatos()
        if datosUsuario != None:
            self.groupBox.hide()
            for i in range(veces):
                codScan = QtGui.QInputDialog.getText(self,"Codigo", "Scanear Codigo de la muestra a ingresar\n " + str(i+1) + " de " + str(veces), QtGui.QLineEdit.Normal)
                if codScan[1] == False :
                    self.close()
                    break
                else:
                    codScan = codScan[0]
                    while ( self.validador.validarCodScan("Codigo Incorrecto",codScan, self) and cvh.controlExistencia(codScan, self) )== False:
                        codScan = QtGui.QInputDialog.getText(self,"Codigo", "Scanear Codigo:", QtGui.QLineEdit.Normal)
                        if codScan[1] == False :
                            self.close()
                            break
                        else:
                            codScan = codScan[0]
                    idmuestra = cvh.insertar(datosUsuario, codScan, operario)  # inserta usuario y muestra. devuelve id de la ultima muestra insertada
                    a = 1
                    while a == 1:

                        self.barra()
                        a = cvh.control(idmuestra)

                                                                                                # se muestra la barra de espera mientras el numero de celda sea 1
            self.groupBox.show()
            self.close()
            QMessageBox.warning(self,"Carga completa", "Muestra cargada correctamente", QMessageBox.Ok)

    def barra(self):
        self.labelCarga.show()
        self.Bcancelar2.show()
        self.progressBar.show()
        self.progressBar.setRange(0, 100000)
        self.progressBar.setValue(0)
        for value in range (0,100000):
            value= value + 0.01

            self.progressBar.setValue(value)
            QtGui.qApp.processEvents()

    def obtenerDatos(self): # obtengo los datos de la vista, paciente
        if self.checkBox.checkState():
            lista = [0,"Anonimo" , "Anonimo",123]
            return lista
        else:

            if self.lineOC.text()== "":
                self.lineOC.setText("0")
            if self.validador.validar_nombre("Completar campo Nombre",self.lineNombre,self,  self.lineNombre.text()) and\
                    self.validador.validar_nombre("Completar campo Apellido", self.lineApellido,self, self.lineApellido.text())and\
                    self.validador.validar_numeros("Completar campo DNI/DU", self.lineDNI,self,  self.lineDNI.text()) and\
                    self.validador.validar_numeros("Completar campo Codigo Paciente", self.lineOC,self,  self.lineOC.text()):
                lista = [ self.lineOC.text(), self.lineNombre.text(), self.lineApellido.text(), self.lineDNI.text()]

                return lista

    def obtenerUsuario(self, u):
        global operario
        operario = u



