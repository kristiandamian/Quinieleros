__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import endpoints
from google.appengine.ext import ndb
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel


class Grupo(EndpointsModel):
    """Grupo con un conjunto de usuarios para una liga"""
    Nombre = ndb.StringProperty()
    usuarios = ndb.KeyProperty(kind="Usuario", repeated=True)

class Usuario(EndpointsModel):
    Nombre = ndb.StringProperty()
    Correo = ndb.StringProperty()

class Liga(EndpointsModel):
    """  """
    NombreLiga = ndb.StringProperty()
    ClaveLiga = ndb.StringProperty()
    Pais = ndb.StringProperty()

class Equipo(ndb.podel):
    Nombre = ndb.StringProperty()
    Apodos = ndb.StringProperty(repeated=True)
    id = ndb.StringProperty()
    liga = ndb.KeyProperty(kind="Liga")

class Calendario(EndpointsModel):
    Nombre = ndb.StringProperty()
    id = ndb.StringProperty()
    FechaInicio = ndb.DateProperty()
    FechaFin = ndb.DateProperty()
    liga = ndb.KeyProperty(kind="Liga")

class Jornada(EndpointsModel):
    Nombre = ndb.StringProperty()
    id = ndb.StringProperty()
    Numero = ndb.IntegerProperty()
    calendario = ndb.KeyProperty(kind="Calendario")

class Partido(EndpointsModel):
    Fecha = ndb.DateProperty()
    Local = ndb.KeyProperty(kind="Equipo")
    Visitante = ndb.KeyProperty(kind="Equipo")
    GolesLocal = ndb.IntegerProperty()
    GolesVisitante = ndb.IntegerProperty()
    jornada = ndb.KeyProperty(kind="Jornada")
    resultado= ndb.StringProperty(default="NO_ESPECIFICADO")
    Info1 = ndb.StringProperty() #Nombre del estadio, ciudad
    Info2 = ndb.StringProperty() #fecha, hora capacidad, etc.

class ResultadosPartido(messages.Enum):
    """Enumerador del resultado"""
    NO_ESPECIFICADO = 1
    GANA_LOCAL = 2
    GANA_VISITANTE = 3
    EMPATE = 4

class ResultadoQuiniela(EndpointsModel):
    usuario = ndb.KeyProperty(kind="Usuario")
    partido = ndb.KeyProperty(kind="Partido")
    resultado = ndb.StringProperty(default="NO_ESPECIFICADO")
    acierto = ndb.BooleanProperty()
    registro = ndb.DateProperty(auto_now_add=True)