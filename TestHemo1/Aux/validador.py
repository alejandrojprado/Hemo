from PyQt4.QtGui import QMessageBox

__author__ = 'ale'
import  re
class validador():

    def validar_nombre(self, mensaje,line,ventana,  textodeline):
        nombre = textodeline
        validar = re.match('^[a-z\s]+$', nombre, re.I)
        if nombre == "":
            line.setStyleSheet("border: 2px solid yellow;")
            self.mensajedeerror(ventana, mensaje)
            return False
        elif not validar:
            mensaje = mensaje + "\nIngresar solo letras de a-z"
            line.setStyleSheet("border: 2px solid red;")
            self.mensajedeerror(ventana, mensaje)
            return False
        else:
            line.setStyleSheet("border: 1px solid green;")
            return True

    def validar_numeros(self, mensaje,line,ventana, numero):
        nombre = numero
        validar = re.match('^[0-9]+$', nombre, re.I)
        if nombre == "":
            line.setStyleSheet("border: 2px solid yellow;")
            self.mensajedeerror(ventana, mensaje)
            return False
        elif not validar:
            line.setStyleSheet("border: 2px solid red;")
            mensaje  = mensaje + "\n Ingresar solo numero (0-9)"
            self.mensajedeerror(ventana, mensaje)
            return False
        elif len(nombre) > 10:
            line.setStyleSheet("border: 2px solid red;")
            mensaje = mensaje + "\n maximo 10 caracteres"
            self.mensajedeerror(ventana, mensaje)
            return False
        else:
            line.setStyleSheet("border: 1px solid green;")
            return True

    def mensajedeerror(self, cosa, mensaje="Error al completar los datos"):
        QMessageBox.warning(cosa,"Error", mensaje, QMessageBox.Ok)

    def validarCodScan(self,mensaje,  numero,ventana ):
        nombre = numero
        validar = re.match('^[0-9]+$', nombre, re.I)
        if nombre == "":
            self.mensajedeerror(ventana, mensaje)
            return False
        elif not validar:
            mensaje  = mensaje + "\n Ingresar solo numero (0-9)"
            self.mensajedeerror(ventana, mensaje)
            return False
        elif len(nombre) > 15:
            mensaje = mensaje + "\n Maximo 15 caracteres"
            self.mensajedeerror(ventana, mensaje)
            return False
        else:
             return True

