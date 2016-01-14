__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import sys
import os
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel

package = 'Quinieleros'

#####class Resultado(EndpointsModel):
#####  """Ejecucion de un resultado de un partido."""
#####  id = ndb.IntegerProperty()
#####  Centro = ndb.StringProperty()
#####  Id_Procedimiento = ndb.IntegerProperty()
#####  FechaInicio = ndb.DateTimeProperty()  ## o deberian ser -> StringField
#####  FechaFin = ndb.DateTimeProperty()     ## o deberian ser -> StringField


#####class ResultadosCollection(EndpointsModel):
#####    items = ndb.StructuredProperty(Resultado, repeated=True)


@endpoints.api(name='quinieleros', version='v1')
class QuinielerosApi(remote.Service):
    """Auditimer API v1."""
    @ResultadosCollection.method(path='resultados', http_method='POST',
                      name='quinieleros.guardarResultados')
    def guardar_resultados(self, request):
        return request

APPLICATION = endpoints.api_server([QuinielerosApi])