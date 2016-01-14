from protorpc import message_types
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel


class GrupoForm(messages.Message):
    displayName = messages.StringField(1)
    usuarios = messages.StringField(2, repeated=True)


GRUPO_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupoKey=messages.StringField(1),
)