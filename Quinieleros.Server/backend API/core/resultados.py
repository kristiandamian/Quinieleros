import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import EquipoMessage, PartidoMessage, JornadaMessage, ResultadosPartido
from endpointsModels import Resultados, Resultado, ResultadoGrupoJornada, ResultadoGrupo
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


def obtener_resultados_grupo(request):
    grupo=Grupo.get_by_id(request.grupoKey) 
    resultados = ResultadoGrupo()
    _match_res=[]
    if grupo!=None:
        jornadas=Jornada.query(Jornada.calendario==grupo.calendario)
        for j in jornadas:
            partidos=Partido.query(Partido.jornada==j.key)
            for usr in grupo.usuarios:
                resultado = ResultadoGrupoJornada()
                resultado.jornada=str( j.Numero)
                resultado.nombre=Usuario.get_by_id(usr.key.id()).Nombre
                resultado.usuario=usr.key.id()
                for p in partidos:
                    res = ResultadoQuiniela.query(ResultadoQuiniela.partido == p.key, usuario = usr)
                    for r in res:
                        if r.acierto:
                            resultado.aciertos = resultado.aciertos+1
                _match_res.append(resultado)
        resultados.nombre=grupo.Nombre
        resultados.resultados=_match_res
    return resultados

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
    usuario=Usuario.get_by_id(usuario)
    respuesta=False
    _resultado_oficial=calculoResultado(golesLocal, golesVisitante)
    if usuario!=None:
        match=Partido.get_by_id(partido.key.id())
        if match!=None:
            res=ResultadoQuiniela.query(ResultadoQuiniela.partido == match.key, ResultadoQuiniela.usuario == usuario.key)
            res=res.get()
            if res!=None:
                if res.resultado!="NO_ESPECIFICADO":
                   acierto = res.resultado==_resultado_oficial
                   if res.acierto==None:
                        res.acierto=acierto
                        res.put()
    return respuesta