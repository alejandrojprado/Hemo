__author__ = 'ale'

from Modelo.usuario import Usuario

class ControladorUsuario:

 def nuevo_usuario(self, lista):
        (unombre, uapellido, uusername, upassword) = lista
        usuario = Usuario()
        usuario.nombre = unombre
        usuario.apellido =uapellido
        usuario.username = uusername
        usuario.password = upassword

        usuario.nuevo()
        #self.UsuarioView.confirmarNuevoUsuario()



