from PyQt4.QtCore import QSize
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from Controlador.controladorVentanaMuestra import ControladorVentanaMuestra

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


class VentanaMuestra(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelEstado = QtGui.QLabel(self.groupBox_2)
        self.labelEstado.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.labelEstado)
        self.labelEstado.setText('Resultado:')
        self.comboBoxResultado = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxResultado.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBoxResultado.setMinimumContentsLength(20)
        self.comboBoxResultado.setObjectName(_fromUtf8("comboBox"))
        self.comboBoxResultado.addItem('todos')
        self.comboBoxResultado.addItem('negativo')
        self.comboBoxResultado.addItem('positivo')
        self.comboBoxResultado.addItem('abortado')
        self.lebelFechas = QtGui.QLabel(self.groupBox_2)
        self.lebelFechas.setText('Fechas')
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setText("Desde")
        self.checkBox2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox2.setText("Hasta")
        self.comboBoxFInicio = QtGui.QPushButton(self.groupBox_2)
        self.comboBoxFInicio.setObjectName(_fromUtf8("comboBox"))
        self.comboBoxFInicio.setText('fecha inicio')
        self.comboBoxFInicio.setEnabled(False)
        self.comboBoxFfin = QtGui.QPushButton(self.groupBox_2)
        self.comboBoxFfin.setObjectName(_fromUtf8("comboBox"))
        self.comboBoxFfin.setText('fecha fin    ')
        self.comboBoxFfin.setEnabled(False)
        self.horizontalLayout.addWidget(self.comboBoxResultado)
        self.horizontalLayout.addWidget(self.lebelFechas)
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalLayout.addWidget(self.comboBoxFInicio)
        self.horizontalLayout.addWidget(self.checkBox2)
        self.horizontalLayout.addWidget(self.comboBoxFfin)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cvm =ControladorVentanaMuestra()
        self.tableview = QTableView()
        self.verticalLayout.addWidget(self.tableview)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.Bcerrar= QtGui.QPushButton(self.groupBox_3)
        self.Bcerrar.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.Bcerrar)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.setWindowTitle('Informe de Muestras')
        self.tableview.setSelectionBehavior(QTableView.SelectRows)
        self.pushButton.setText('Buscar')

        self.Bcerrar.setText('Cerrar')
        self.Bcerrar.setMinimumSize(QtCore.QSize(180, 75))
        self.Bcerrar.setMaximumSize(QtCore.QSize(180, 75))
        iconoCerrar = QtGui.QIcon("/home/pi/TestHemo1/img/cerrar.png")
        self.Bcerrar.setIcon(iconoCerrar)
        self.Bcerrar.setIconSize(QSize(30,30))
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL( "textChanged(QString)"),self.buscar)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.buscar)
        QtCore.QObject.connect(self.comboBoxFfin, QtCore.SIGNAL(_fromUtf8("clicked()")),self.elegirFechaFin)
        QtCore.QObject.connect(self.comboBoxFInicio, QtCore.SIGNAL(_fromUtf8("clicked()")),self.elegirFechaInicio)
        QtCore.QObject.connect(self.Bcerrar, QtCore.SIGNAL(_fromUtf8("clicked()")),self.cerrarVentana)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accionCheck)
        QtCore.QObject.connect(self.checkBox2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accionCheck)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("selectionStart()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.tableview, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.llamadorVentanaMuestrasHistorico)
        self.lineEdit.setPlaceholderText('Ingresar DNI de paciente')
        self.buscar()
        self.horizontalLayout_2.addWidget(self.Bcerrar)
        self.comboBoxFfin


    def llamadorVentanaMuestrasHistorico(self):
        from Vista.VentanaMuestraHistorial import VentanaMuestraHistorial
        index = self.tableview.selectedIndexes()[6]
        valorClick = self.tableview.model().data(index).toString()
        self.vmh = VentanaMuestraHistorial(valorClick)
        self.vmh.showFullScreen()
        self.close()

    def elegirFechaInicio(self):
        self.boton = self.sender()
        self.selectDates()


    def elegirFechaFin(self):
        self.boton = self.sender()
        self.selectDates()


    def selectDates(self):
        self.dateWindow = QWidget()
        self.cal = QCalendarWidget(self)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.cal)
        self.dateWindow.setLayout(self.hbox)
        self.dateWindow.setGeometry(100, 100, 350, 300)
        self.dateWindow.setWindowTitle('Elegir Fecha')
        self.dateWindow.show()


    def showDate(self):
        fecha = self.cal.selectedDate()
        fechaTexto = fecha.toString('yyyy-M-d')
        self.boton.setText(fechaTexto)
        self.dateWindow.close()


    def buscar(self):
        self.tableview.setModel(self.cvm.busqueda(self.lineEdit.text(), self.comboBoxResultado.currentText(), self.comboBoxFInicio.text(), self.comboBoxFfin.text()))

    def cerrarVentana(self):
        self.close()

    def accionCheck(self):
        if self.checkBox2.isChecked():
            self.comboBoxFfin.setEnabled(True)
        else:
            self.comboBoxFfin.setEnabled(False)
            self.comboBoxFfin.setText('fecha fin    ')

        if self.checkBox.isChecked():
            self.comboBoxFInicio.setEnabled(True)
        else:

            self.comboBoxFInicio.setEnabled(False)
            self.comboBoxFInicio.setText('fecha inicio')
