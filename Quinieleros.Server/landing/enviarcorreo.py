from google.appengine.api import mail

def enviarCorreo(nombre, correo, phone, mensaje):
	mail.send_mail(sender="serviciosvilla.com Support <serviciosvilla88@gmail.com>",
		       to="kristian <kristiandamian@gmail.com>",
		       subject="Un nuevo comentario en serviciosvilla.com de: "+nombre,
                       body="""
	Hola Patricia:

	Hay un nuevo comentario en serviciosvilla.com:

	Nombre: """+nombre+"""
	Correo: """+correo+"""
	Telefono: """+phone+"""
	Mensaje: """+mensaje+"""

        Saludos""")
