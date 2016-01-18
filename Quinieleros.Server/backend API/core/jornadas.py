import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage
from models import Grupo, Usuario, Calendario, Liga, Equipo, Partido, Jornada

def buscar_jornada(request):
    jornada=Jornada.query(calendario == request.calendariokey, Numero = int(request.jornada), abierto=True)
    jm = JornadaMessage()
    partidosJornada = []
    if jornada!=None:
        partidos=Partido.query(jornada==jornada.key)
        if partidos!=None:
            for p in partidos:
                partido=PartidoMessage()
                partido.Fecha = p.Fecha
                partido.Info1 = p.Info1
                partido.Info2 = p.Info2
                partido.key = p.key.id()
                local= EquipoMessage()
                l=Equipo.get_by_id(p.Local)
                if l!=None:
                    local.Nombre=l.Nombre
                    local.key=l.key.id
                    visitante=EquipoMessage()
                v=Equipo.get_by_id(p.Visitante)
                if v!=None:
                    visitante.Nombre=v.Nombre
                    visitante.key=v.key.id
                
                partido.Local = local
                partido.Visitante = visitante
                partidosJornada.append(partido)
        jm.key = jornada.key.id()
        jm.Nombre=jornada.Nombre
        jm.partidos = partidosJornada
    return jm