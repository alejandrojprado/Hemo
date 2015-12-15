import time

__author__ = 'ale'

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanitaAlarma.ui'
#
# Created: Thu Sep 17 14:40:13 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMainWindow, QWidget, QDialog
from Controlador.controladorVentanitaAlarma import ControladorVentanitaAlarma
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

class VentanaPositivo(QMainWindow):

    def __init__(self, celda, celdaString, colorenVentanita):
        QMainWindow.__init__(self)
        self.celdaString = celdaString
        self.celda = celda
        self.colorVentanita = colorenVentanita
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.resize(604, 398)
        MainWindow.setStyleSheet(_fromUtf8(self.colorVentanita))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(565, 310, 241, 71))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 130, 451, 61))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.cva = ControladorVentanitaAlarma()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.celdaMasFecha(self.cva.consultas(self.celda))
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Aceptar", None))
        self.label.setText(_translate("MainWindow", str(self.celdaString), None))
        font	 = QtGui.QFont("arial",20,True)
        self.label.setFont(font)
        self.label.setStyleSheet('color: white')

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        self.cva.updateAC(self.celda)
        self.close()

    def celdaMasFecha(self, fecha):
        if fecha != None:
            fecha =fecha.strftime("%d/%m/%Y") +"       "+fecha.strftime("%H:%M")
            self.celdaString = self.celdaString + "\n\n           " + fecha