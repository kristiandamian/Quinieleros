__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from core.grupos import grabar_grupo, buscar_grupo, buscar_grupos
from core.ligas import buscar_ligas
from core.calendarios import buscar_calendarios
from core.jornadas import buscar_jornada
from core.resultados import guardar_resultados, get_resultados_grupo
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import LigasMessage,LigasMessageCollection
from endpointsModels import CalendarioMessage, CalendarioMessageCollection
from endpointsModels import JornadaMessage, PartidoMessage
from endpointsModels import Resultados, Resultado
from endpointsModels import GRUPO_GET_REQUEST, JORNADA_GET_REQUEST

package = 'Quinieleros'

@endpoints.api(name='quinieleros', version='v1', description='API restful para el sitio quinieleros.com')
class QuinielerosApi(remote.Service):
    """API restful para el sitio quinieleros.com"""

    #######################     GRUPOS     #######################
    @endpoints.method(GrupoForm, BooleanMessage,
                    path='grupos/add', http_method='POST',
                    name='generar_grupo')
    def save_grupo(self, grupo):
       return grabar_grupo(grupo)

    @endpoints.method(GRUPO_GET_REQUEST, GrupoMessage,
                  path='grupos/{grupoKey}', http_method='GET',
                  name='obtener_grupo') 
    def get_grupo(self, request):
        return buscar_grupo(request)

    @endpoints.method(GRUPO_GET_REQUEST, GrupoMessageCollection,
                  path='grupos/all/{grupoKey}', http_method='GET',
                  name='obtener_grupos_del_usuario')
    def get_grupo_byUser(self, request):
        return buscar_ligas(request)
    #######################     LIGAS      #######################
    @endpoints.method(message_types.VoidMessage, LigasMessageCollection,
                  path='ligas/all', http_method='GET',
                  name='obtener_todas_las_ligas')
    def get_ligas(self, request):
        return buscar_ligas(request)
    #######################   CALENDARIOS  #######################
    @endpoints.method(GRUPO_GET_REQUEST, CalendarioMessageCollection,
                  path='ligas/{grupoKey}/calendarios', http_method='GET',
                  name='obtener_calendarios_de_una_liga')
    def get_calendarios(self, request):
        return buscar_calendarios(request)
    #######################    JORNADAS    #######################
    @endpoints.method(JORNADA_GET_REQUEST, JornadaMessage,
                  path='ligas/{ligaKey}/{calendariokey}/{jornada}/{usuario}/', http_method='GET',
                  name='obtener_jornada')
    def get_jornada(self, request):
        return buscar_jornada(request)
    #######################   RESULTADOS   #######################
    @endpoints.method(Resultados, BooleanMessage,
                  path='ligas/resultados', http_method='POST',
                  name='guardar_resultados')
    def save_resultados(self, request):
        return guardar_resultados(request)

    #def get_resultados_grupo
APPLICATION = endpoints.api_server([QuinielerosApi])