import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import GRUPO_GET_REQUEST
from models import Grupo, Usuario, Calendario

def grabar_grupo(grupo):
    usrs=[]
    error=False
    msg=""
    try:
        for user in grupo.usuarios:
            usr=Usuario.get_or_insert(user)
            usr.Correo = user
            usr.put()
            usrs.append(usr.key)
        cal=Calendario.get_by_id(grupo.calendarioKey)
        if cal!=None:
            _grp=Grupo()
            _grp.Nombre=grupo.Nombre
            _grp.usuarios=usrs 
            _grp.calendario = cal.key
            _grp.put()
        else:
            error=True
            msg="No existe el calendario"
    except Exception, ex:
        error=True
        msg= str(ex)
    return BooleanMessage(error=error, mensaje=msg)

def buscar_grupo(request):
    grupo=Grupo.get_by_id(int(request.grupoKey))
    respuesta=GrupoMessage()
    if grupo!=None:
        respuesta.Nombre=grupo.Nombre
        respuesta.key = str(grupo.key.id())
    return respuesta

def buscar_grupos(request):
    usr = Usuario.get_by_id(request.grupoKey)
    _gpos=[]
    if usr != None: 
        grupos=Grupo.query(Grupo.usuarios == usr.key)
            
        if grupos!=None:
            for grupo in grupos:
                _gpo = GrupoMessage()
                _gpo.Nombre=grupo.Nombre
                _gpo.key = str(grupo.key.id())
                _gpos.append(_gpo)
    respuesta=GrupoMessageCollection(grupos=_gpos)
    return respuesta