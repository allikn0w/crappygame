#!/usr/bin/python3

import os
import optparse
from random import randint
from random import choice
from time import sleep

def Play():
  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir');

class ListarPersonajes(object):
  def __init__(self):
    

class Personaje(object):
  def __init__(self,personaje):
    self.personaje = personaje

  def Cargar_Personaje(self):
    with open('personajes') as f:
      lines = f.redlines()
 
def main():
  parser = optparse.OptionParser()
  parser.add_option('-p','--personaje',
    action="store", dest="personaje", help="elige tu personaje")

  options,args = parser.parse_args()
  print('Personaje elegido: ', options.personaje)
  

  print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir');
  
  {'P':pelear(),
   'C':cargar(),
   'B':borrar(),
   'N':crear()}[option]()




  
if __name__ == '__main__':
  main()
