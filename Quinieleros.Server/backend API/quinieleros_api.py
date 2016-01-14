__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from endpointsModels import GrupoForm
from endpointsModels import GRUPO_GET_REQUEST
from models import Grupo

package = 'Quinieleros'

@endpoints.api(name='quinieleros', version='v1', description='API restful para el sitio quinieleros.com')
class QuinielerosApi(remote.Service):
    """API restful para el sitio quinieleros.com"""

    #######################   GRUPOS   #######################
    @endpoints.method(GrupoForm, message_types.BooleanMessage,
                    path='grupos/add', http_method='POST',
                    name='quinieleros.generargrupo')
    def greetings_list(self, grupo):
        return grupo

    @endpoints.method(GRUPO_GET_REQUEST,
                  path='grupos/{grupoKey}', http_method='GET',
                  name='quinieleros.obtenergrupo')
    def get_grupo(self, request):
        return request


APPLICATION = endpoints.api_server([QuinielerosApi])