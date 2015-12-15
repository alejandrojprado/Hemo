#!/usr/bin/env python
__author__ = 'ale'
import sys
from time import  time,sleep
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Vista.ventanaPrincipal import VentanaPrincipal



def main(argv):
        app = QApplication(argv, True)
        vp=VentanaPrincipal()
        vp.showFullScreen()
        app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
        sys.exit(app.exec_())



if __name__ == "__main__":
        main(sys.argv)



