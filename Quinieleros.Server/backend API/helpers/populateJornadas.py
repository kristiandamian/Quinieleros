import os
import pprint
import time
from datetime import datetime
from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.ext import db
from models import Grupo, Usuario, Liga, Calendario, Equipo, Jornada, Partido

def addJornadas():
    l=Liga.get_by_id("ligamx")
    c=Calendario.get_by_id("Clausura2016")
    #### // EQUIPOS
    america=Equipo.get_by_id("America")
    atlas=Equipo.get_by_id("Atlas")
    america=Equipo.get_by_id("America")
    chiapas=Equipo.get_by_id("Chiapas")
    cruzazul=Equipo.get_by_id("CruzAzul")
    dorados=Equipo.get_by_id("Dorados")
    chivas=Equipo.get_by_id("Chivas")
    leon=Equipo.get_by_id("Leon")
    monterrey=Equipo.get_by_id("Monterrey")
    morelia=Equipo.get_by_id("Morelia")
    pachuca=Equipo.get_by_id("Pachuca")
    puebla=Equipo.get_by_id("Puebla")
    pumas=Equipo.get_by_id("PumasUNAM")
    queretaro=Equipo.get_by_id("Queretaro")
    santos=Equipo.get_by_id("Santos")
    tigres=Equipo.get_by_id("Tigres")
    toluca=Equipo.get_by_id("Toluca")
    tijuana=Equipo.get_by_id("Tijuana")
    veracruz=Equipo.get_by_id("Veracruz")
    ### JORNADA 1
    j=Jornada.get_by_id("jornada01")

    p=Partido.get_or_insert(queretaro.key.id()+atlas.key.id()+c.key.id())
    p.Fecha = datetime.strptime("8/01/2016","%d/%m/%Y")
    p.Local = queretaro.key
    p.Visitante = atlas.key
    p.GolesLocal = 1
    p.GolesVisitante = 3
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(tijuana.key.id()+pachuca.key.id()+c.key.id())
    p.Fecha = datetime.strptime("8/01/2016","%d/%m/%Y")
    p.Local = tijuana.key
    p.Visitante = pachuca.key
    p.GolesLocal = 1
    p.GolesVisitante = 1
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(america.key.id()+puebla.key.id()+c.key.id())
    p.Fecha = datetime.strptime("9/01/2016","%d/%m/%Y")
    p.Local = america.key
    p.Visitante = puebla.key
    p.GolesLocal = 0
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(monterrey.key.id()+pumas.key.id()+c.key.id())
    p.Fecha = datetime.strptime("9/01/2016","%d/%m/%Y")
    p.Local = monterrey.key
    p.Visitante = pumas.key
    p.GolesLocal = 1
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(leon.key.id()+santos.key.id()+c.key.id())
    p.Fecha = datetime.strptime("9/01/2016","%d/%m/%Y")
    p.Local = leon.key
    p.Visitante = santos.key
    p.GolesLocal = 2
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(morelia.key.id()+cruzazul.key.id()+c.key.id())
    p.Fecha = datetime.strptime("9/01/2016","%d/%m/%Y")
    p.Local = morelia.key
    p.Visitante = cruzazul.key
    p.GolesLocal = 2
    p.GolesVisitante = 2
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(chiapas.key.id()+dorados.key.id()+c.key.id())
    p.Fecha = datetime.strptime("9/01/2016","%d/%m/%Y")
    p.Local = chiapas.key
    p.Visitante = dorados.key
    p.GolesLocal = 1
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(toluca.key.id()+pumas.key.id()+c.key.id())
    p.Fecha = datetime.strptime("10/01/2016","%d/%m/%Y")
    p.Local = toluca.key
    p.Visitante = pumas.key
    p.GolesLocal = 1
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(chivas.key.id()+veracruz.key.id()+c.key.id())
    p.Fecha = datetime.strptime("10/01/2016","%d/%m/%Y")
    p.Local = chivas.key
    p.Visitante = veracruz.key
    p.GolesLocal = 2
    p.GolesVisitante = 2
    p.jornada = j.key
    p.put()

    ### JORNADA 2
    j=Jornada.get_by_id("jornada02")

    p=Partido.get_or_insert(veracruz.key.id()+leon.key.id()+c.key.id())
    p.Fecha = datetime.strptime("15/01/2016","%d/%m/%Y")
    p.Local = veracruz.key
    p.Visitante = leon.key
    p.GolesLocal = 1
    p.GolesVisitante = 3
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(santos.key.id()+chiapas.key.id()+c.key.id())
    p.Fecha = datetime.strptime("15/01/2016","%d/%m/%Y")
    p.Local = santos.key
    p.Visitante = chiapas.key
    p.GolesLocal = 1
    p.GolesVisitante = 3
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(cruzazul.key.id()+chivas.key.id()+c.key.id())
    p.Fecha = datetime.strptime("16/01/2016","%d/%m/%Y")
    p.Local = cruzazul.key
    p.Visitante = chivas.key
    p.GolesLocal = 1
    p.GolesVisitante = 1
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(tigres.key.id()+morelia.key.id()+c.key.id())
    p.Fecha = datetime.strptime("16/01/2016","%d/%m/%Y")
    p.Local = tigres.key
    p.Visitante = morelia.key
    p.GolesLocal = 2
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(pachuca.key.id()+queretaro.key.id()+c.key.id())
    p.Fecha = datetime.strptime("16/01/2016","%d/%m/%Y")
    p.Local = pachuca.key
    p.Visitante = queretaro.key
    p.GolesLocal = 1
    p.GolesVisitante = 0
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(atlas.key.id()+america.key.id()+c.key.id())
    p.Fecha = datetime.strptime("16/01/2016","%d/%m/%Y")
    p.Local = atlas.key
    p.Visitante = america.key
    p.GolesLocal = 0
    p.GolesVisitante = 3
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(dorados.key.id()+tijuana.key.id()+c.key.id())
    p.Fecha = datetime.strptime("16/01/2016","%d/%m/%Y")
    p.Local = dorados.key
    p.Visitante = tijuana.key
    p.GolesLocal = 0
    p.GolesVisitante = 1
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(pumas.key.id()+toluca.key.id()+c.key.id())
    p.Fecha = datetime.strptime("17/01/2016","%d/%m/%Y")
    p.Local = pumas.key
    p.Visitante = toluca.key
    p.GolesLocal = 3
    p.GolesVisitante = 2
    p.jornada = j.key
    p.put()

    p=Partido.get_or_insert(puebla.key.id()+monterrey.key.id()+c.key.id())
    p.Fecha = datetime.strptime("17/01/2016","%d/%m/%Y")
    p.Local = puebla.key
    p.Visitante = monterrey.key
    p.GolesLocal = 1
    p.GolesVisitante = 3
    p.jornada = j.key
    p.put()