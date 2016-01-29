
import os
import urllib
import jinja2
import webapp2
import json
import cgi
from google.appengine.ext import ndb
from webapp2 import WSGIApplication, Route
from webapp2_extras.routes import DomainRoute
import sys
from auth.secrets import SESSION_KEY
from auth.handlers import InicioSesion
from core.grupos import gruposHandler
from core.calendarios import calendarioHandler
from core.estadisticas import estadisticasHandler
from core.Privacidad import AvisoPrivacidad, TerminosYCondiciones
import logging

# Se agrega el directorio './lib' el ruta para poder hacer "import ndb"
if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']
if 'auth' not in sys.path:
    sys.path[0:0] = ['auth']

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

	    
#configuracion de webapp2
app_config = {
  'webapp2_extras.sessions': {
    'cookie_name': '_simpleauth_sess',
    'secret_key': SESSION_KEY
  },
  'webapp2_extras.auth': {
    'user_attributes': []
  }
}
#manejo de rutas de la app
routes = [   
  Route('/', InicioSesion),
  Route('/avisoPrivacidad', AvisoPrivacidad),
  Route('/terminosyCondiciones', TerminosYCondiciones),
  Route('/calendario/<grupo:(\d+)>/',calendarioHandler),
  Route('/estadisticas/<grupo:(\d+)>/',estadisticasHandler),
  Route('/profile',gruposHandler, name="profile"),
  Route('/logout', handler='handlers.AuthHandler:logout', name='logout'),
  Route('/auth/<provider>',handler='handlers.AuthHandler:_simple_auth', name='auth_login'),
  Route('/auth/<provider>/callback',
      handler='handlers.AuthHandler:_auth_callback', name='auth_callback')
]


app = webapp2.WSGIApplication(routes, config=app_config, debug=True)