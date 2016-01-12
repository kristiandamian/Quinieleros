import os
import urllib
import jinja2
import webapp2
import main
import logging
from auth.handlers import BaseRequestHandler

class AvisoPrivacidad(BaseRequestHandler):
        def get(self):
	    self.render('avisoprivacidad.html')

class TerminosYCondiciones(BaseRequestHandler):
        def get(self):
	    self.render('terminosycondiciones.html')