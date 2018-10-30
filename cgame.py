#!/usr/bin/python3

import os
import optparse
from random import randint
from random import choice
from time import sleep
'''
class adf(object):
  def __init__(self):
    

  def xx(self,,,):
'''  
  
def main():
  parser = optparse.OptionParser()
  parser.add_option('-p','--personaje',
    action="store", dest="personaje", help="elige tu personaje")

  options,args = parser.parse_args()
  print('Personaje elegido: ', options.personaje)







  
if __name__ == '__main__':
  main()
