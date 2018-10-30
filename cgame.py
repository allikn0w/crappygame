#!/usr/bin/python3
import os
import optparse
from random import randint
from random import choice
from time import sleep
import json

class Personaje(object):
  def __init__(self,personaje):
    self.personaje = personaje

  def Opciones(self):
    print('[P]elear, [C]argar, [N]uevo personaje, [B]orrar, [S]alir')
  
  def ListarPersonajes(self):
    self.names = json.loads(open('personajes.json').read())['personajes']
    for name in self.names:
      print ("+ {}".format(name["name"]))

  def C(self):
    print('Ingrese el personaje:')
    self.personaje = input()
    for name in self.names:
      if name["name"] == self.personaje:
        data = name
        self.vida = data["vida"]
        self.escudo = data["escudo"]
        self.mana = data["mana"]
        self.ataque = data["ataque"]
        self.defensa = data["defensa"]
        print(name)
    print("Cargado!")

  def P(self):
    print('Pelear')

  def B(self):
    print('Borrar')

  def N(self):
    print('Crear') 

  def notAfun(self):
    print('No existe esa accion')

  def Acciones(self,jugada):
    {'P':self.P,
    'C':self.C,
    'B':self.B,
    'N':self.N}.get(jugada, self.notAfun)()
  

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

  Jugador.Opciones()
  jugada = input()
  Jugador.Acciones(jugada)



  
if __name__ == '__main__':
  main()
