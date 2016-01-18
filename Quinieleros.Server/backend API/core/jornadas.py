import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from core.resultados import calculoResultado, es_acierto
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage, ResultadosPartido
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
                partido.acierto = es_acierto(request.usuario, p, p.GolesLocal, p.GolesVisitante)
                partido.resultado = calculoResultado(p.GolesLocal, p.GolesVisitante)
                partido.GolesLocal=p.GolesLocal
                partido.GolesVisitante=p.GolesVisitante
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