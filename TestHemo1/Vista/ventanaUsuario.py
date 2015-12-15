# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaUsuario.ui'
#
# Created: Wed Aug 19 16:47:23 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QMainWindow
from PyQt4.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from Vista.ventanaMuestra import VentanaMuestra

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

class VentanaUsuario(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


    def setupUi(self, VentanaUsuario):
        VentanaUsuario.setObjectName(_fromUtf8("VentanaUsuario"))
        VentanaUsuario.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VentanaUsuario.setWindowModality(QtCore.Qt.ApplicationModal)
        VentanaUsuario.resize(769, 623)
        self.centralwidget = QtGui.QWidget(VentanaUsuario)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.GgrupBox = QtGui.QGroupBox(self.centralwidget)
        self.GgrupBox.setTitle(_fromUtf8(""))
        self.GgrupBox.setObjectName(_fromUtf8("GgrupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.GgrupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.GContenedores = QtGui.QGroupBox(self.GgrupBox)
        self.GContenedores.setTitle(_fromUtf8(""))
        self.GContenedores.setObjectName(_fromUtf8("GContenedores"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.GContenedores)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.GNuevoUsuario = QtGui.QGroupBox(self.GContenedores)
        self.GNuevoUsuario.setObjectName(_fromUtf8("GNuevoUsuario"))
        self.verticalLayout = QtGui.QVBoxLayout(self.GNuevoUsuario)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelName = QtGui.QLabel(self.GNuevoUsuario)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.verticalLayout.addWidget(self.labelName)
        self.lineEditNombre = QtGui.QLineEdit(self.GNuevoUsuario)
        self.lineEditNombre.setObjectName(_fromUtf8("lineEditNombre"))
        self.verticalLayout.addWidget(self.lineEditNombre)
        self.labelApellido = QtGui.QLabel(self.GNuevoUsuario)
        self.labelApellido.setObjectName(_fromUtf8("labelApellido"))
        self.verticalLayout.addWidget(self.labelApellido)
        self.lineEditApellido = QtGui.QLineEdit(self.GNuevoUsuario)
        self.lineEditApellido.setObjectName(_fromUtf8("lineEditApellido"))
        self.verticalLayout.addWidget(self.lineEditApellido)
        self.labelUsuario = QtGui.QLabel(self.GNuevoUsuario)
        self.labelUsuario.setObjectName(_fromUtf8("labelUsuario"))
        self.verticalLayout.addWidget(self.labelUsuario)
        self.lineEditUsuario = QtGui.QLineEdit(self.GNuevoUsuario)
        self.lineEditUsuario.setObjectName(_fromUtf8("lineEditUsuario"))
        self.verticalLayout.addWidget(self.lineEditUsuario)
        self.labelContrasea = QtGui.QLabel(self.GNuevoUsuario)
        self.labelContrasea.setObjectName(_fromUtf8("labelContrasea"))
        self.verticalLayout.addWidget(self.labelContrasea)
        self.lineEditContrasea = QtGui.QLineEdit(self.GNuevoUsuario)
        self.lineEditContrasea.setObjectName(_fromUtf8("lineEditContrasea"))
        self.verticalLayout.addWidget(self.lineEditContrasea)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_2 = QtGui.QSplitter(self.GNuevoUsuario)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.BSubmit = QtGui.QPushButton(self.splitter_2)
        self.BSubmit.setObjectName(_fromUtf8("BSubmit"))
        self.BClear = QtGui.QPushButton(self.splitter_2)
        self.BClear.setObjectName(_fromUtf8("BClear"))
        self.verticalLayout.addWidget(self.splitter_2)
        self.horizontalLayout_4.addWidget(self.GNuevoUsuario)
        self.GUsuarios = QtGui.QGroupBox(self.GContenedores)
        self.GUsuarios.setObjectName(_fromUtf8("GUsuarios"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.GUsuarios)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = QtGui.QTableView(self.GUsuarios)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.splitter = QtGui.QSplitter(self.GUsuarios)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.BDelet = QtGui.QPushButton(self.splitter)
        self.BDelet.setObjectName(_fromUtf8("BDelet"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_4.addWidget(self.GUsuarios)
        self.verticalLayout_3.addWidget(self.GContenedores)
        self.groupBox_2 = QtGui.QGroupBox(self.GgrupBox)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(560, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.BCerrar = QtGui.QPushButton(self.groupBox_2)

        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.horizontalLayout_2.addWidget(self.BCerrar)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.GgrupBox)
        VentanaUsuario.setCentralWidget(self.centralwidget)


        self.retranslateUi(VentanaUsuario)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEditContrasea.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEditUsuario.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEditApellido.clear)
        QtCore.QObject.connect(self.BClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEditNombre.clear)
        QtCore.QObject.connect(self.BDelet, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tableView.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(VentanaUsuario)

        ####################################
        iconoCerrar = QtGui.QIcon("/home/pi/TestHemo1/img/cerrar.png")
        self.BCerrar.setIcon(iconoCerrar)
        self.BCerrar.setIconSize(QSize(30,30))
        self.BCerrar.setMinimumSize(QtCore.QSize(180, 75))
        self.llenarTabla()

    def llenarTabla(self):
        self.modelo = QSqlTableModel(self)
        self.modelo.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.modelo.setTable("operario")
        self.modelo.select()
        self.tableView.setModel(self.modelo)
        self.tableView.selectionBehavior()
        self.tableView.setColumnHidden(1,True)
        self.tableView.setColumnHidden(0,True)
        self.tableView.setColumnHidden(5,True)

    def retranslateUi(self, VentanaUsuario):
        VentanaUsuario.setWindowTitle(_translate("VentanaUsuario", "Usuario", None))
        self.GNuevoUsuario.setTitle(_translate("VentanaUsuario", "Nuevo Usuario", None))
        self.labelName.setText(_translate("VentanaUsuario", "Nombre", None))
        self.labelApellido.setText(_translate("VentanaUsuario", "Apellido", None))
        self.labelUsuario.setText(_translate("VentanaUsuario", "Usuario", None))
        self.labelContrasea.setText(_translate("VentanaUsuario", "Contraseña", None))
        self.BSubmit.setText(_translate("VentanaUsuario", "Aceptar", None))
        self.BClear.setText(_translate("VentanaUsuario", "Borrar", None))
        self.GUsuarios.setTitle(_translate("VentanaUsuario", "Usuarios", None))
        self.BDelet.setText(_translate("VentanaUsuario", "Borrar", None))
        self.BCerrar.setText(_translate("VentanaUsuario", "Cerrar", None))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCerrar.sizePolicy().hasHeightForWidth())
        self.BCerrar.setSizePolicy(sizePolicy)

        iconoCerrar = QtGui.QIcon("/home/ale/PycharmProjects/TestHemo1/img/cerrar.png")
        self.BCerrar.setIcon(iconoCerrar)
        self.BCerrar.setIconSize(QSize(30,30))
        self.BCerrar.setMinimumSize(QtCore.QSize(130, 75))

    @QtCore.pyqtSlot()
    def on_BCerrar_clicked(self):
        self.close()
        self.BClear.click()


    @QtCore.pyqtSlot()
    def on_BSubmit_clicked(self):
        from Controlador.controladorVentanaUsuario import ControladorUsuario
        cvu = ControladorUsuario()
        datos = [self.lineEditNombre.text(),
        self.lineEditApellido.text(),
        self.lineEditUsuario.text(),
        self.lineEditContrasea.text()]
        cvu.nuevo_usuario(datos)
        self.BClear.click()
        self.llenarTabla()

    @QtCore.pyqtSlot()
    def on_BDelet_clicked(self):
        self.modelo.removeRow(self.tableView.currentIndex().row())


    def obtenerUsuario(self, usuario):
        if usuario != "admin":
            self.tableView.setEnabled(False)
        else:
            self.tableView.setEnabled(True)
