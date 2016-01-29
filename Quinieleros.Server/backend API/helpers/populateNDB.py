import os
import pprint
import time
from datetime import datetime
from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.ext import db
from models import Grupo, Usuario, Liga, Calendario, Equipo

#LIGA
l=Liga.get_or_insert("ligamx")
l.NombreLiga="Liga MX"
l.Clave="ligamx"
l.Pais="mexico"
l.put()

#CALENDARIO
l=Liga.get_or_insert("ligamx")
c=Calendario.get_or_insert("Clausura2016")
c.Nombre = "Clausura 2016"
c.id = "Clausura2016"
c.FechaInicio = datetime.strptime("8/01/2016","%d/%m/%Y")
c.FechaFin =  datetime.strptime("8/05/2016","%d/%m/%Y")
c.liga = l.key
c.abierto = True
c.put()

#Grupo

#EQUIPOS
l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("America")
e.Apodos=["Los Azulcremas", "El Ame", "Los millonetas", "Las aguilas" ]
e.Nombre="America"
e.liga=l.key
e.put()

l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Atlas")
e.Apodos=["Los Zorros", "Los Rojinegros" ]
e.Nombre="Atlas"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Chiapas")
e.Apodos=[ "Jaguares"  ]
e.Nombre="Chiapas"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("CruzAzul")
e.Apodos=[ "La maquina", "Los Cementeros" ]
e.Nombre="Cruz Azul"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Dorados")
e.Apodos=[ "El gran pez", "los Dorados" ]
e.Nombre="Dorados de Sinaloa"
e.liga=l.key
e.put()
#.... AQUI ME QUEDE
#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Chivas")
e.Apodos=[ "Rebaño sagrado","Rojiblancos", "Chivas"  ]
e.Nombre="Chivas"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Leon")
e.Apodos=[ "Los panzas verdes","Los esmeraldas", "Leon" ]
e.Nombre="Leon"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Monterrey")
e.Apodos=[  "Los rayados","La pandilla" ]
e.Nombre="Monterrey"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Morelia")
e.Apodos=[ "La monarquia","Los Purepechas"  ]
e.Nombre="Morelia"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Pachuca")
e.Apodos=[ "Los tuzos" ]
e.Nombre="Pachuca"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Puebla")
e.Apodos=["La franja","Los camoteros"]
e.Nombre="Puebla"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("PumasUNAM")
e.Apodos=["Pumas", "Felinos", "Auriazules","Los del pedregal"]
e.Nombre="Pumas UNAM"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Queretaro")
e.Apodos=[ "Los Gallos Blancos" ]
e.Nombre="Queretaro"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Santos")
e.Apodos=[ "Los laguneros", "Los guerreros" ]
e.Nombre="Santos"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Tigres")
e.Apodos=[ "Tigres","Los felinos" ]
e.Nombre="Tigres"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Tijuana")
e.Apodos=[ "Los Xolos","La jauria", "El Xolaje" ]
e.Nombre="Tijuana"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Toluca")
e.Apodos=["Diablos Rojos","El equipo escarlata","Los choriceros" ]
e.Nombre="Toluca"
e.liga=l.key
e.put()

#l=Liga.get_or_insert("ligamx")
e=Equipo.get_or_insert("Veracruz")
e.Apodos=["El Tiburon","Los escualos"]
e.Nombre="Veracruz"
e.liga=l.key
e.put()

 #################### JORNADAS ########################################################
if Jornada.query().count()==0: #Solo la primera vez
    l=Liga.get_or_insert("ligamx")
    c=Calendario.get_or_insert("Clausura2016")
    j=Jornada.get_or_insert("jornada01")
    j.Nombre = "jornada 1"
    j.Numero = 1
    j.FechaMaxima = datetime.strptime("8/01/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = False
    j.put()

    j=Jornada.get_or_insert("jornada02")
    j.Nombre = "jornada 2"
    j.Numero = 2
    j.FechaMaxima = datetime.strptime("15/01/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = False
    j.put()

    j=Jornada.get_or_insert("jornada03")
    j.Nombre = "jornada 3"
    j.Numero = 3
    j.FechaMaxima = datetime.strptime("22/01/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada04")
    j.Nombre = "jornada 4"
    j.Numero = 4
    j.FechaMaxima = datetime.strptime("29/01/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada05")
    j.Nombre = "jornada 5"
    j.Numero = 5
    j.FechaMaxima = datetime.strptime("5/02/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada06")
    j.Nombre = "jornada 6"
    j.Numero = 6
    j.FechaMaxima = datetime.strptime("12/02/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada07")
    j.Nombre = "jornada 7"
    j.Numero = 7
    j.FechaMaxima = datetime.strptime("19/02/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada08")
    j.Nombre = "jornada 8"
    j.Numero = 8
    j.FechaMaxima = datetime.strptime("26/02/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada09")
    j.Nombre = "jornada 9"
    j.Numero = 9
    j.FechaMaxima = datetime.strptime("4/03/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada10")
    j.Nombre = "jornada 10"
    j.Numero = 10
    j.FechaMaxima = datetime.strptime("11/03/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada11")
    j.Nombre = "jornada 11"
    j.Numero = 11
    j.FechaMaxima = datetime.strptime("18/03/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada12")
    j.Nombre = "jornada 12"
    j.Numero = 12
    j.FechaMaxima = datetime.strptime("1/04/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada13")
    j.Nombre = "jornada 13"
    j.Numero = 13
    j.FechaMaxima = datetime.strptime("8/04/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada14")
    j.Nombre = "jornada 14"
    j.Numero = 14
    j.FechaMaxima = datetime.strptime("15/04/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada15")
    j.Nombre = "jornada 15"
    j.Numero = 15
    j.FechaMaxima = datetime.strptime("22/04/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada16")
    j.Nombre = "jornada 16"
    j.Numero = 16
    j.FechaMaxima = datetime.strptime("29/04/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()

    j=Jornada.get_or_insert("jornada17")
    j.Nombre = "jornada 17"
    j.Numero = 17
    j.FechaMaxima = datetime.strptime("6/05/2016","%d/%m/%Y")
    j.calendario = c.key
    j.abierto = True
    j.put()
