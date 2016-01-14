__author__ = 'kristiandamian@gmail.com (Kristian Damian)'

import sys
import os

#AGREGO LA CARPETA endpoints-proto-datastore PARA PODER USARLO EN APP ENGINE

ENDPOINTS_PROJECT_DIR = os.path.join(os.path.dirname(__file__),
                                     'endpoints-proto-datastore')
sys.path.append(ENDPOINTS_PROJECT_DIR)