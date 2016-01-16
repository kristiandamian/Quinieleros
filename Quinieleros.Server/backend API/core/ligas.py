import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import GRUPO_GET_REQUEST
from endpointsModels import LigasMessage,LigasMessageCollection
from models import Grupo, Usuario, Calendario, Liga

def buscar_ligas(request):
    ligas = Liga.query().fetch(20)
    ligas_vigentes=[]
    if ligas != None: 
        for liga in ligas:
            lm=LigasMessage()
            lm.Nombre=liga.NombreLiga
            lm.key=liga.key.id()
            ligas_vigentes.append(lm)
    respuesta=LigasMessageCollection(ligas=ligas_vigentes)
    return respuesta