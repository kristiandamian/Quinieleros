import sys
import os
import endpoints
from datetime import datetime
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from core.resultados import calculoResultado, es_acierto
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage, ResultadosPartido, NumeroJornadaMessageCollection, NumeroJornadaMessage 
from models import Grupo, Usuario, Calendario, Liga, Equipo, Partido, Jornada

def buscar_jornada(request):
    partidosJornada = []
    jm = JornadaMessage()
    grupo=Grupo.get_by_id(int(request.grupokey))
    if grupo!=None:
        jornada=Jornada.query(Jornada.calendario == grupo.calendario, Jornada.Numero == int(request.jornada))
        jornada=jornada.get()
        if jornada!=None:
            
            partidos=Partido.query(Partido.jornada==jornada.key)
            if partidos!=None:
                for p in partidos:
                    partido=PartidoMessage()
                    partido.Fecha = p.Fecha.strftime('%d/%m/%Y')
                    partido.Info1 = p.Info1
                    partido.Info2 = p.Info2
                    partido.key = p.key.id()
                    partido.acierto = es_acierto(request.usuario, p, p.GolesLocal, p.GolesVisitante)
                    partido.resultado = calculoResultado(p.GolesLocal, p.GolesVisitante)
                    partido.GolesLocal=p.GolesLocal
                    partido.GolesVisitante=p.GolesVisitante
                    partido.jornadaAbierta=jornada.abierto
                    local= EquipoMessage()
                    l=Equipo.get_by_id(p.Local.id())
                    if l!=None:
                        local.Nombre=l.Nombre
                        local.key=l.key.id()
                    visitante=EquipoMessage()
                    v=Equipo.get_by_id(p.Visitante.id())
                    if v!=None:
                        visitante.Nombre=v.Nombre
                        visitante.key=v.key.id()
                
                    partido.Local = local
                    partido.Visitante = visitante
                    partidosJornada.append(partido)
            jm.key = jornada.key.id()
            jm.Nombre=jornada.Nombre
            jm.partidos = partidosJornada
    return jm

def buscar_jornadas(request):
    grupo=Grupo.get_by_id(int(request.grupokey))

    jornadas = []
    if grupo!=None:
        jornada=Jornada.query(Jornada.calendario == grupo.calendario)
        if jornada!=None:
            for j in jornada:
                jm = NumeroJornadaMessage()
                jm.Abierta=j.abierto
                jm.Nombre="J"+str(j.Numero)#j.Nombre
                jm.Numero=j.Numero
                jornadas.append(jm)
    respuesta=NumeroJornadaMessageCollection(jornadas=jornadas)
    return respuesta
