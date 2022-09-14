Para que funcione tienes que crear una clave secreta, para ello crea un archivo llamado en primerapp/primaraapp/secret.py con:
SECRET_KEY = ''
y entre comillas pegas el resultado de ejecutar python generador_django.py
Aunque este código no lo voy a reusar y solo lo tengo para practicas, considero que esta forma de comartirlo es mejor por si alguien termina subiendo algun derivado del código