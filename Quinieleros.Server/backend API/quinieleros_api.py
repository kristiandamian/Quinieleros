__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from core.grupos import grabar_grupo, buscar_grupo, buscar_grupos
from endpointsModels import GrupoForm, BooleanMessage, GrupoMessage, GrupoMessageCollection
from endpointsModels import GRUPO_GET_REQUEST

package = 'Quinieleros'

@endpoints.api(name='quinieleros', version='v1', description='API restful para el sitio quinieleros.com')
class QuinielerosApi(remote.Service):
    """API restful para el sitio quinieleros.com"""

    #######################   GRUPOS   #######################
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
        return buscar_grupos(request)



APPLICATION = endpoints.api_server([QuinielerosApi])