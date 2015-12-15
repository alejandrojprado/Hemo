from PyQt4.QtCore import QSize
from PyQt4.QtGui import QMainWindow, QTableView
from Controlador.controladorVentanaMuestra import ControladorVentanaMuestra
from Aux.validador import validador
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPaciente.ui'
#
# Created: Wed Sep  9 10:30:12 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class VentanaPacientes(QMainWindow):

    def __init__(self):
        self.validador = validador()
        self.cvm = ControladorVentanaMuestra()
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 800)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.splitter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.splitter)
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.GpacienteDatos = QtGui.QGroupBox(self.groupBox_2)
        self.GpacienteDatos.setObjectName(_fromUtf8("GpacienteDatos"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.GpacienteDatos)
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
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
        spacerItem = QtGui.QSpacerItem(20, 262, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.splitter_2 = QtGui.QSplitter(self.GpacienteDatos)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pushButton = QtGui.QPushButton(self.splitter_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Bcrear = QtGui.QPushButton(self.splitter_2)
        self.Bcrear.setObjectName(_fromUtf8("Bcrear"))
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout_2.addWidget(self.GpacienteDatos)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(563, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.BCerrar = QtGui.QPushButton(self.groupBox_3)
        self.BCerrar.setMinimumSize(QtCore.QSize(180, 75))
        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.horizontalLayout.addWidget(self.BCerrar)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #############################
        iconoCerrar = QtGui.QIcon("/home/pi/TestHemo1/img/cerrar.png")
        self.BCerrar.setIcon(iconoCerrar)
        self.BCerrar.setIconSize(QSize(30,30))
        self.BCerrar.setMinimumSize(QtCore.QSize(180, 75))
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL( "textChanged(QString)"),self.buscar)
        QtCore.QObject.connect(self.BCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cerrarVentana)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("selectionStart()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.tableView, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.asignacionPaciente)
        self.BCerrar.setText("Cerrar")
        self.lineEdit.setPlaceholderText('DNI/DU Paciente')
        self.buscar()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pcientes", None))
        self.groupBox.setTitle(_translate("MainWindow", "Pacientes Existentes", None))
        self.label.setText(_translate("MainWindow", "Buscar por DNI/DU", None))
        self.label_2.setText(_translate("MainWindow", "* Doble click sobre paciente existente para asignar         ", None))
        self.GpacienteDatos.setTitle(_translate("MainWindow", "Crear nuevo paciente", None))
        self.pacienteNombre.setText(_translate("p.dni as DNI,MainWindow", "Nombre", None))
        self.pacienteApellido.setText(_translate("MainWindow", "Apellido", None))
        self.pacienteDNI.setText(_translate("MainWindow", "DU/DNI", None))
        self.pacienteCodInterno.setText(_translate("MainWindow", "Otro codigo", None))
        self.pushButton.setText(_translate("MainWindow", "Editar", None))
        self.Bcrear.setText(_translate("MainWindow", "Crear", None))



    def asignacionPaciente(self):
        index = self.tableView.selectedIndexes()[2]
        valorClick = self.tableView.model().data(index).toString()
        self.cvm.actualizarPaciente(valorClick, self.idMuestra)
        self.close()
        from Vista.VentanaMuestraHistorial import VentanaMuestraHistorial
        self.vmh = VentanaMuestraHistorial(self.idMuestra)
        self.vmh.showMaximized()


    def obtenerIdMuestra(self, muestra):
        self.idMuestra = muestra

    def buscar(self):
        self.tableView.setModel(self.cvm.busquedaPaciente(self.lineEdit.text()))

    def cerrarVentana(self):
        self.close()

    @QtCore.pyqtSlot()
    def on_Bcrear_clicked(self):
        from Controlador.controladorVentanaPaciente import ControladorVentanaPaciente
        self.cvp = ControladorVentanaPaciente()
        if self.validador.validar_nombre("Completar campo Nobre\nIngresar solo letras de a-z",self.lineNombre,self,  self.lineNombre.text()) and\
                    self.validador.validar_nombre("Completar campo Apellido\n Ingresar solo letras de a-z", self.lineApellido,self, self.lineApellido.text())and\
                    self.validador.validar_numeros("Completar campo DNI/DU\n Ingresar solo numero del 0-9", self.lineDNI,self,  self.lineDNI.text()) and\
                    self.validador.validar_numeros("Completar campo Codigo Paciente\n Ingresar solo numero del 0-9", self.lineOC,self,  self.lineOC.text()):
            listaDatos = []
            listaDatos.append(self.lineNombre.text())
            listaDatos.append(self.lineApellido.text())
            listaDatos.append(self.lineDNI.text())
            listaDatos.append(self.lineOC.text())
            self.cvp.nuevoPaciente(listaDatos)
            self.buscar()