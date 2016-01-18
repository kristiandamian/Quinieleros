import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage, ResultadosPartido
from endpointsModels import Resultados, Resultado
from models import Grupo, Usuario, Calendario, Liga, Equipo, Partido, Jornada, ResultadoQuiniela


def guardar_resultados(request):
    calendario=Calendario.get_by_id(request.calendariokey)
    respuesta=BooleanMessage()
    if calendario!=None:
        usuario=Usuario.get_by_id(request.correo)
        if usuario!=None:
            for match in request.resultados:
                partido=Partido.get_by_id(match.partido)
                if partido!=None:
                    _key=partido.Local.id()+"vs"+partido.Visitante.id()+calendario.key.id()
                    res=ResultadoQuiniela.get_or_insert(_key)
                    res.usuario=usuario.key
                    res.partido=partido.key
                    res.resultado=match.resultado
                    res.put()
        else:
            respuesta.error=True
            respuesta.mensaje="No esta registrado el usuario "+request.correo
    else:
        respuesta.error=True
        respuesta.mensaje="No existe el calendario"
    return respuesta


def get_resultados_grupo(request):
    pass 


def calculoResultado(golesLocal, golesVisitante):
    respuesta="NO_ESPECIFICADO"
    golesLocal=int(golesLocal)
    golesVisitante=int(golesVisitante)
    if golesLocal==golesVisitante :
        respuesta="EMPATE"
    elif golesLocal>golesVisitante:
        respuesta="GANA_LOCAL"
    else:
        respuesta="GANA_VISITANTE"
    return respuesta

def es_acierto(usuario,partido, golesLocal, golesVisitante):
    usuario=Usuario.get_by_id(request.correo)
    respuesta=False
    _resultado_oficial=calculoResultado(golesLocal, golesVisitante)
    if usuario!=None:
        match=Partido.get_by_id(match.partido)
        if match!=None:
            res=ResultadoQuiniela.query(ResultadoQuiniela.partido == match, ResultadoQuiniela.usuario == usuario)
            if res!=None:
                res=res.get()
                if res.resultado!="NO_ESPECIFICADO":
                   acierto = res.resultado==_resultado_oficial
                   if res.acierto==None:
                        res.acierto=acierto
                        res.put()
    return respuesta