import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import CalendarioMessage, CalendarioMessageCollection
from endpointsModels import GRUPO_GET_REQUEST
from models import Grupo, Usuario, Calendario, Liga

def buscar_calendarios(request):
    liga = Liga.get_by_id(request.grupoKey)
    calendarios=[]
    if liga != None: 
        cals=Calendario.query(Calendario.liga == liga.key, Calendario.abierto == True)
        for c in cals:
            calendario=CalendarioMessage()
            calendario.Nombre=c.Nombre
            calendario.key=c.key.id()
            calendarios.append(calendario)
    respuesta=CalendarioMessageCollection(calendarios=calendarios)
    return respuesta