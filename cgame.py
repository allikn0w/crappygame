#!/usr/bin/python3

import os
import optparse
from random import randint
from random import choice
from time import sleep
import json


def Play():
  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir');

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
      print ("+"  + name["name"])
    print("\n")


  def C(self):
    print('Cargar')

  def P(self):
    print('Pelear')

  def B(self):
    print('Borrar')

  def N(self):
    print('Crear') 

  def notAfun(self):
    print('No existe esa accion')

  def Acciones(self,accion):
    {'P':self.P,
    'C':self.C,
    'B':self.B,
    'N':self.N}.get(accion, self.notAfun)()
  

class Perfiles(object):
  def __init__(self):
    names = json.loads(open('personajes.json').read())
    print(names.get("andresito"))

 
def main():
  parser = optparse.OptionParser()
  parser.add_option('-p','--personaje',
    action="store", dest="personaje", help="elige tu personaje")

  options,args = parser.parse_args()
  print('Personaje elegido: %s \n' % options.personaje)

  Jugador = Personaje(options.personaje)
  
  if options.personaje is None:
    print('Mostrando personajes existentes:')
    Jugador.ListarPersonajes()

  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir')
  accion = input()
  Jugador.Acciones(accion)



  
if __name__ == '__main__':
  main()
