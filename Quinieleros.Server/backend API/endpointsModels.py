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
    #######################################################################
    acierto = messages.BooleanField(7) 
    resultado=messages.StringField(8)  
    GolesLocal = messages.IntegerField(9) 
    GolesVisitante = messages.IntegerField(19) 
    jornadaAbierta = messages.BooleanField(20) 
    NombreUsuario = messages.StringField(21)
    CorreoUsuario = messages.StringField(22)

class JornadaMessage(messages.Message):
    Nombre = messages.StringField(1)
    key = messages.StringField(2)
    partidos = messages.MessageField(PartidoMessage, 3, repeated=True)

class NumeroJornadaMessage(messages.Message):
    Numero = messages.IntegerField(1)
    Nombre = messages.StringField(2)
    Abierta = messages.BooleanField(3)

class NumeroJornadaMessageCollection(messages.Message):
    jornadas = messages.MessageField(NumeroJornadaMessage, 1, repeated=True)

class Resultado(messages.Message):
    partido = messages.StringField(1)
    resultado = messages.EnumField('ResultadosPartido', 2)

class Resultados(messages.Message):
    calendariokey=messages.StringField(1)
    resultados = messages.MessageField(Resultado, 2, repeated=True)
    correo = messages.StringField(3)
    grupo = messages.IntegerField(4)

class ResultadoGrupoJornada(messages.Message):
    jornada=messages.StringField(1)
    aciertos=messages.IntegerField(2)
    usuario=messages.StringField(3)
    nombre=messages.StringField(4)

class ResultadoGrupo(messages.Message):
    nombre=messages.StringField(1)
    resultados = messages.MessageField(ResultadoGrupoJornada, 2, repeated=True)

GRUPO_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupoKey=messages.StringField(1),
)


GRUPO_JORNADA_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupoKey=messages.StringField(1),
     jornada=messages.StringField(2),
)
JORNADA_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupokey=messages.StringField(2),
    jornada=messages.StringField(3),
    usuario=messages.StringField(4),
)

JORNADA_MIN_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    grupokey=messages.StringField(1),
)

RESULTADO_GET_REQUEST = endpoints.ResourceContainer(
    message_types.VoidMessage,
    calendariokey=messages.StringField(1),
    jornada=messages.StringField(2),
)


class ResultadosPartido(messages.Enum):
    """Enumerador del resultado"""
    NO_ESPECIFICADO = 1
    GANA_LOCAL = 2
    GANA_VISITANTE = 3
    EMPATE = 4
