#!/usr/bin/python3

import os
import optparse
from random import randint
from random import choice
from time import sleep
import json


def Play():
  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir');

'''
class ListarPersonajes(object):
  def __init__(self):
'''      

class Personaje(object):
  def __init__(self,personaje):
    self.personaje = personaje

  '''
  def Cargar_Personaje(self):
    with open('personajes') as f:
      lines = f.redlines()
  '''
  def ListarPersonajes(self):
    names = json.loads(open('personajes.json').read())
    for name in names['personajes']:
      print (name["name"])

  def Cargar(self):
    

  def Acciones(self):
    pass

class Perfiles(object):
  def __init__(self):
    names = json.loads(open('personajes.json').read())
    print(names.get("andresito"))

 
def main():
  parser = optparse.OptionParser()
  parser.add_option('-p','--personaje',
    action="store", dest="personaje", help="elige tu personaje")

  options,args = parser.parse_args()
  print('Personaje elegido: ', options.personaje)

  Jugador = Personaje(options.personaje)
  
  if options.personaje is None:
    print('No elegiste ningún jugador con el parámetro -p. Mostrando personajes existentes:')
    Jugador.ListarPersonajes()

  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir');
  
  '''
  {'P':pelear(),
   'C':cargar(),
   'B':borrar(),
   'N':crear()}[option]()
  '''



  
if __name__ == '__main__':
  main()
