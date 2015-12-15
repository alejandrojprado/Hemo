from PyQt4.QtCore import QSize
from PyQt4.QtGui import QMainWindow
from datetime import timedelta, datetime
import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg


__author__ = 'ale'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaMestraHistorial.ui'
#
# Created: Thu Sep  3 00:34:19 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controlador.controladorVistaDatos import ControladorVistaDatos
from Vista.VentanaPacientes import VentanaPacientes
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

class VentanaMuestraHistorial(QMainWindow):

    def __init__(self, idmuestra):
        QMainWindow.__init__(self)
        self.idMuestra = idmuestra
        self.vp = VentanaPacientes()
        self.cvmh = ControladorVistaDatos()
        self.setupUi(self, self.idMuestra)

    def setupUi(self,VentanaMuestraHistorial, muestra):

        VentanaMuestraHistorial.setObjectName(_fromUtf8("VentanaMestraHistorial"))
        VentanaMuestraHistorial.resize(1088, 676)
        VentanaMuestraHistorial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(VentanaMuestraHistorial)
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
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.GpacienteDatos = QtGui.QGroupBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GpacienteDatos.sizePolicy().hasHeightForWidth())
        self.GpacienteDatos.setSizePolicy(sizePolicy)
        self.GpacienteDatos.setObjectName(_fromUtf8("GpacienteDatos"))
        self.verticalLayout = QtGui.QVBoxLayout(self.GpacienteDatos)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.GpacienteDatos)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_8 = QtGui.QLabel(self.splitter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Basignar = QtGui.QPushButton(self.splitter)
        self.Basignar.setMaximumSize(QtCore.QSize(190, 20))
        self.Basignar.setObjectName(_fromUtf8("Basignar"))
        self.verticalLayout.addWidget(self.splitter)
        self.label_9 = QtGui.QLabel(self.GpacienteDatos)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.GpacienteDatos)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
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

        self.splitter_2 = QtGui.QSplitter(self.groupBox_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))

        self.label_11 = QtGui.QLabel(self.splitter_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))


        self.BObservar = QtGui.QPushButton(self.splitter_2)
        self.BObservar.setMaximumSize(QtCore.QSize(190, 20))
        self.BObservar.setObjectName(_fromUtf8("BObservar"))
        self.verticalLayout_5.addWidget(self.splitter_2)



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
        spacerItem = QtGui.QSpacerItem(20, 472, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)

        self.BCerrar = QtGui.QPushButton(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCerrar.sizePolicy().hasHeightForWidth())
        self.BCerrar.setSizePolicy(sizePolicy)
        self.Bgraficar = QtGui.QPushButton(self.splitter_2)
        self.Bgraficar.setSizePolicy(sizePolicy)
        self.Bgraficar.setMinimumSize(QtCore.QSize(0, 75))
        self.Bgraficar.setObjectName(_fromUtf8("Bgraficar"))
        self.verticalLayout_6.addWidget(self.Bgraficar)

        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.verticalLayout_6.addWidget(self.BCerrar)
        self.horizontalLayout.addWidget(self.groupBox_4)
        VentanaMuestraHistorial.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaMuestraHistorial)
        QtCore.QMetaObject.connectSlotsByName(VentanaMuestraHistorial)
        QtCore.QObject.connect(self.Basignar, QtCore.SIGNAL("clicked()"), self.asignar)
        iconoCerrar = QtGui.QIcon("/home/pi/TestHemo1/img/cerrar.png")
        self.BCerrar.setIcon(iconoCerrar)
        self.BCerrar.setIconSize(QSize(30,30))
        self.BCerrar.setMinimumSize(QtCore.QSize(180, 75))
        self.traerdatos(muestra)
        self.graficar()
        QtCore.QObject.connect(self.Bgraficar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hacerGrafico)


    def retranslateUi(self, VentanaMestraHistorial):
        VentanaMestraHistorial.setWindowTitle(_translate("VentanaMestraHistorial", "Detalle Celda", None))
        self.GpacienteDatos.setTitle(_translate("VentanaMestraHistorial", "Datos del paciente", None))
        self.label_8.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.Basignar.setText(_translate("VentanaMestraHistorial", "Asignar Paciente", None))
        self.BObservar.setText(_translate("VentanaMestraHistorial", "Agregar Observaciones", None))
        self.label_9.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_10.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.groupBox_3.setTitle(_translate("VentanaMestraHistorial", "Datos de la muestra", None))
        self.label.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_2.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_3.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_5.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_4.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_6.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_7.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.label_11.setText(_translate("VentanaMestraHistorial", "TextLabel", None))
        self.BCerrar.setText(_translate("VentanaMestraHistorial", "Cerrar", None))
        self.Bgraficar.setText(_translate("VentanaMestraHistorial", "Graficar", None))

    def graficar(self,tiempo=[datetime.now(),datetime.now()],curva=[0,1]):
        self.c1 = FigureCanvasQTAgg(matplotlib.figure.Figure())
        axes = self.c1.figure.add_subplot(111)
        axes.plot(tiempo, curva, lw="3")
        axes.set_autoscaley_on(False)                                         # limites de axes
        axes.set_ylim([0,110])
        axes.set_xlim(tiempo[0], tiempo[0]+timedelta(days=5))
        axes.set_xlabel('Horas', fontsize=16)
        axes.set_ylabel("Desvio", fontsize = 16)
        self.verticalLayout_3.addWidget(self.c1)
        self.c1.show()

    def hacerGrafico(self):

        valoresGrafico = self.cvmh.valoresGrafico(self.idMuestra)
        tiempo = valoresGrafico[0]
        curva = valoresGrafico[1]
        self.c1.close()
        self.graficar(tiempo, curva)
    def traerdatos(self, muestra):

        listaDatos = self.cvmh.traerDatos(muestra)
        if listaDatos[0] == "Anonimo":
            self.label_8.setText("Nombre : " +str(listaDatos[0]))
            self.label_9.setText("DNI/DU : Desconocido")
            self.label_10.setText("Codigo : Desconocido")
        else:
            self.label_8.setText("Nombre : " +str(listaDatos[0])+" "+str(listaDatos[1]))
            self.label_9.setText("DNI/DU : " + str(listaDatos[2]))
            self.label_10.setText("Codigo : " + str(listaDatos[3]))
        self.label.setText("Fecha ingreso : "+ str(listaDatos[4]))

        self.label_2.setText("Fecha egreso : "+str(listaDatos[5]))
        if listaDatos[6] == None:
            listaDatos[6] = "Sin Resultado"

        self.label_3.setText("Fecha resultado : "+str(listaDatos[6] ))
        self.label_4.setText("Resultado : "+ str(listaDatos[7]))
        self.label_5.setText("Tiempo de analisis : " + str(listaDatos[8]))
        self.label_6.setText("codigo Frasco : " +str(listaDatos[9]))
        self.label_7.setText("Operario  : " +str(listaDatos[10]))
        self.label_11.setText("Observaciones  : " +str(listaDatos[11]))

    def asignar(self):
            self.vp.obtenerIdMuestra(self.idMuestra)
            self.vp.show()
            self.close()

    @QtCore.pyqtSlot()
    def on_BCerrar_clicked(self):
            self.close()