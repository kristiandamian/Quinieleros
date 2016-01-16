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
    calendarioKey = messages.IntegerField(3)

class LigasMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)

class LigasMessageCollection(messages.Message):
    """Colleccion de LigasMessage."""
    ligas = messages.MessageField(LigasMessage, 1, repeated=True)

class CalendarioMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)

class CalendarioMessageCollection(messages.Message):
    """Colleccion de CalendarioMessage."""
    calendarios = messages.MessageField(CalendarioMessage, 1, repeated=True)

class EquipoMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)

class PartidoMessage(messages.Message):
    Fecha = messages.StringField(1)
    Local = messages.MessageField(EquipoMessage, 2)
    Visitante = messages.MessageField(EquipoMessage, 3)
    Info1 = messages.StringField(4)
    Info2 = messages.StringField(5)
    key = messages.StringField(6)

class JornadaMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)
    partidos = messages.MessageField(PartidoMessage, 3, repeated=True)


GRUPO_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupoKey=messages.StringField(1),
)

JORNADA_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    ligaKey=messages.StringField(1),
    calendariokey=messages.StringField(2),
    jornada=messages.StringField(3),
)

class ResultadosPartido(messages.Enum):
    """Enumerador del resultado"""
    NO_ESPECIFICADO = 1
    GANA_LOCAL = 2
    GANA_VISITANTE = 3
    EMPATE = 4