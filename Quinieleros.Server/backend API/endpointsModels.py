import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


class BooleanMessage(messages.Message):
    """BooleanMessage-- outbound Boolean value message"""
    error = messages.BooleanField(1)
    mensaje= messages.StringField(2)

    
class GrupoMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)

class GrupoMessageCollection(messages.Message):
  """Colleccion de GrupoMessage."""
  grupos = messages.MessageField(GrupoMessage, 1, repeated=True)


class GrupoForm(messages.Message):
    Nombre = messages.StringField(1)
    usuarios = messages.StringField(2, repeated=True)


GRUPO_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupoKey=messages.StringField(1),
)

class ResultadosPartido(messages.Enum):
    """Enumerador del resultado"""
    NO_ESPECIFICADO = 1
    GANA_LOCAL = 2
    GANA_VISITANTE = 3
    EMPATE = 4