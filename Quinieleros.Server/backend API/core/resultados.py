import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage
from models import Grupo, Usuario, Calendario, Liga, Equipo, Partido, Jornada


def save_resultados(request):
    pass

def get_resultados(request):
    pass

def get_resultados_grupo(request):
    pass 