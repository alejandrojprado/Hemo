# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCelda.ui'
#
# Created: Thu Aug 27 20:39:27 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from datetime import datetime, timedelta
from PyQt4.QtCore import QSize, pyqtSignal
from PyQt4.QtGui import QMainWindow, QMessageBox

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from Controlador.controladorVentanaCelda import ControladorVentanaCelda


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

class VentanaCelda(QMainWindow):

    def __init__(self,parent=None):
        QMainWindow.__init__(self)

        self.cvc = ControladorVentanaCelda()
        #self.obtenerCelda(celda)
        self.setupUi(self)

        #self.graficar()
        #self.obtenerDatos()

    def setupUi(self, VentanaCelda):
        VentanaCelda.setObjectName(_fromUtf8("VentanaCelda"))
        VentanaCelda.setWindowModality(QtCore.Qt.ApplicationModal)
        VentanaCelda.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VentanaCelda.resize(800, 600)
        VentanaCelda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(VentanaCelda)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.numeroCelda = QtGui.QLabel(self.groupBox_5)
        self.numeroCelda.setObjectName(_fromUtf8("numeroCelda"))
        self.verticalLayout_3.addWidget(self.numeroCelda)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.GpacienteDatos = QtGui.QGroupBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GpacienteDatos.sizePolicy().hasHeightForWidth())
        self.GpacienteDatos.setSizePolicy(sizePolicy)
        self.GpacienteDatos.setObjectName(_fromUtf8("GpacienteDatos"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.GpacienteDatos)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.GpacienteDatos)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.GpacienteDatos)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.GpacienteDatos)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_2.addWidget(self.GpacienteDatos)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)

        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_5.addWidget(self.label_11)

        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)


        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.Bextender = QtGui.QPushButton(self.groupBox_4)
        self.Bextender.setObjectName(_fromUtf8("Bextender"))
        self.verticalLayout_6.addWidget(self.Bextender)
        self.Bretirar = QtGui.QPushButton(self.groupBox_4)
        self.Bretirar.setMinimumSize(QtCore.QSize(0, 75))
        self.Bretirar.setObjectName(_fromUtf8("Bretirar"))
        self.verticalLayout_6.addWidget(self.Bretirar)
        spacerItem = QtGui.QSpacerItem(20, 472, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.Bcerrar = QtGui.QPushButton(self.groupBox_4)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bcerrar.sizePolicy().hasHeightForWidth())

        self.Bcerrar.setSizePolicy(sizePolicy)
        self.Bcerrar.setMinimumSize(QtCore.QSize(0, 75))

        #self.Bcerrar.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.Bcerrar.setObjectName(_fromUtf8("Bcerrar"))
        self.verticalLayout_6.addWidget(self.Bcerrar)

        self.horizontalLayout.addWidget(self.groupBox_4)
        VentanaCelda.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaCelda)
        QtCore.QMetaObject.connectSlotsByName(VentanaCelda)
##############################################################################################

        self.celda = 0
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(50, 250, 1270, 50)
        self.progressBar.setFormat("Comprobando Extraccion de la muestra")
        self.progressBar.hide()
        self.Bcerrar.setText("  Cerrar    ")
        iconoCerrar = QtGui.QIcon("/home/pi/TestHemo1/img/cerrar.png")
        self.Bcerrar.setIcon(iconoCerrar)
        self.Bcerrar.setIconSize(QSize(30,30))
        iconoSacar = QtGui.QIcon("/home/pi/TestHemo1/img/sacar.png")
        self.Bretirar.setIcon(iconoSacar)
        self.Bretirar.setIconSize(QSize(30,30))
        self.Bcancelar2 = QtGui.QPushButton(self)
        self.Bcancelar2.setGeometry(330, 500, 700, 30)
        self.Bcancelar2.setObjectName(_fromUtf8("Bcancelar2"))
        self.Bcancelar2.setText("Cancelar extraccion")
        self.Bcancelar2.hide()
        self.labelCarga = QtGui.QLabel(self)
        self.labelCarga.setText("Completando extraccion. Aguarde")
        self.labelCarga.setGeometry(550, 230, 700, 30)
        self.labelCarga.setObjectName(_fromUtf8("labelCarga"))
        self.labelCarga.setText("Comprobando extraccion de la muestra\n        "
                                "          aguarde un momento")
        QtCore.QTimer.singleShot(1000, self.hacerGrafico)
        self.labelCarga.hide()
        QtCore.QObject.connect(self.Bextender, QtCore.SIGNAL(_fromUtf8("clicked()")), self.extender)
        QtCore.QObject.connect(self.Bcerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.Bcancelar2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancelar)

    def retranslateUi(self, VentanaCelda):
        VentanaCelda.setWindowTitle(_translate("VentanaCelda", "Detalle Celda", None))
        self.GpacienteDatos.setTitle(_translate("VentanaCelda", "Datos del paciente", None))
        self.label_8.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_9.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_10.setText(_translate("VentanaCelda", "TextLabel", None))
        self.groupBox_3.setTitle(_translate("VentanaCelda", "Datos de la muestra", None))
        self.label.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_2.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_3.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_4.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_5.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_6.setText(_translate("VentanaCelda", "TextLabel", None))
        self.label_7.setText(_translate("VentanaCelda", "TextLabel", None))
        self.Bretirar.setText(_translate("VentanaCelda", "Retirar Muestra", None))
        self.Bextender.setText(_translate("VentanaCelda", "Extender Analisis", None))
        self.Bcerrar.setText(_translate("VentanaCelda", "Cerrar ", None))

    def obtenerCelda(self,celdaa):
        self.celda= celdaa [1: ]
        valores =self.cvc.obtenerIdCelda(celdaa[1:])
        self.idCelda = valores[0]
        return valores[2]

    def cancelar(self):
        self.cvc.cancelar()

    def obtenerDatos(self):
        listaDatos = self.cvc.valoresTablasCelda(self.celda)
        if listaDatos == None:
            self.GpacienteDatos.hide()
            self.groupBox_3.close()
            self.groupBox_2.close()
            self.numeroCelda.setText("Celda "+str(self.celda)+ " - datos de Muestra no cargados".upper())
            self.Bretirar.setEnabled(False)
            self.Bextender.setEnabled(False)
        else:
            if listaDatos[0] == "Anonimo":
                self.label_8.setText("Nombre : " +str(listaDatos[0]))
                self.label_9.setText("DNI/DU : Desconocido")
                self.label_10.setText("Codigo : Desconocido")
            else:
                self.label_8.setText("Nombre : " +str(listaDatos[0])+" "+str(listaDatos[1]))
                self.label_9.setText("DNI/DU : " + str(listaDatos[2]))
                self.label_10.setText("Codigo : " + str(listaDatos[3]))

            self.label.setText("Fecha ingreso : "+ str(listaDatos[4]))
            self.label_2.setText("Estado : "+str(listaDatos[5]))
            tiempoendias= listaDatos[6]/1440
            self.label_3.setText("Tiempo de analisis : "+ str(tiempoendias) + " dias")
            self.label_4.setText("Tiempo transcurrido : "+str(listaDatos[7] ))
            self.label_5.setText("Codigo frasco : "+ str(listaDatos[8]))
            self.label_6.setText("Operario : " + str(listaDatos[9]))
            self.label_7.setText("Observaciones : " +str(listaDatos[10]))
            if listaDatos[11]!= None:
                self.label_11.setText("Fecha deteccion resultado: " + str(listaDatos[11]))
                self.label_12.setText("Tiempo Trascurrido desde resultado: " + str(listaDatos[12]))

    def graficar(self,tiempo=[datetime.now(),datetime.now()],curva=[0,1],tick = False):

        self.c1 = FigureCanvasQTAgg(matplotlib.figure.Figure())
        axes = self.c1.figure.add_subplot(111)

        axes.plot(tiempo, curva,lw="3")
        axes.set_autoscaley_on(False)                                             # limites de axes
        axes.set_ylim([-2,110])
        axes.set_xlim(tiempo[0], tiempo[0]+timedelta(days=5))
        axes.set_xlabel('Horas', fontsize=16)
        axes.set_ylabel("Desvio", fontsize = 16)
        axes.get_xaxis().set_visible(tick)
        self.verticalLayout_3.addWidget(self.c1)

        self.c1.show()

        font= QtGui.QFont("arial",20,True)
        self.numeroCelda.setText("Celda "+str(self.celda).upper())
        self.numeroCelda.setFont(font)

    def hacerGrafico(self):
        cvc = ControladorVentanaCelda()
        valoresGrafico = cvc.valoresGrafico(self.idCelda )
        tiempo = valoresGrafico[0]
        curva = valoresGrafico[1]
        self.c1.close()
        self.graficar(tiempo, curva,True)

    @QtCore.pyqtSlot()
    def on_Bretirar_clicked(self):

        self.centralwidget.hide()
        codScan = QtGui.QInputDialog.getText(self,"Codigo", "Scanear codigo de muestra. celda numero " + str(self.celda), QtGui.QLineEdit.Normal)
        if codScan[1] == False :
            self.close()
        else:
                if codScan[0] != "":
                    codScan = codScan[0]
                    if self.cvc.habilitarBaja(self.celda, codScan) == True:
                        self.labelCarga.show()
                        self.cvc.retirar(self.celda)
                        self.close()
                        QMessageBox.warning(self,"Extraccion completa", "Muestra retirada correctamente", QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self,"Error", "Se retiro muestra de celda incorrecta.\nReintente el procedimiento", QMessageBox.Ok)
                        self.close()
                else:
                    QMessageBox.warning(self,"Error", "Se retiro muestra de celda incorrecta.\nReintente el procedimiento", QMessageBox.Ok)
                    self.close()

    def extender(self):
        tiempo = QtGui.QInputDialog.getText(self,"Extender", "Ingresar cantidad de dias:", QtGui.QLineEdit.Normal)
        tiempo = int(tiempo[0])
        self.label_3.setText("Tiempo de analisis : " + str(tiempo)+ " dias")
        self.cvc.extender(tiempo, self.celda)


