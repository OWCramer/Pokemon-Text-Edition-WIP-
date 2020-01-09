''' fight prototype'''
import pokemon_moves
import random
from random import randint

class Enemy_poke_name_here():
  def name():
    print ("Test_enemy_name")
  def move1():
    print ("ET1")
    Eattack = 5
  def move2():
    print ("ET2")
    Eattack = 10
  def move3():
    print ("ET3")
    Eattack = 15
  def move4():
    print ("ET4")
    Eattack = 20
  def Health():
    Ehealth = 50
  
class Poke_name_here():
  def name():
    print ("test_name")
  def Moves():
    move_list = [move1(), move2(), move3(), move4()]
  def move1():
    print ("AT1")
  def move2():
    print ("AT2")
  def move3():
    print ("AT3")
  def move4():
    print ("AT4")
  def Health():
    health = 50

def fight():
  Ehealth = 0
  #global Enemy_poke_name_here.Health()
  global move_list
  #global Ehealth
  Enemy_poke_name_here.Health()
  print()
  print()
  print("[fight] [Run] [Bag] [Pokemon]")
  option1 = input(": ").lower()
  if option1 == "fight":
    print (move_list)
    if option1 == "AT1":
      attack = 10
      print("attack hit!")
    if critchance == True:
      print ("critical hit")
      attack = attack *2
      Ehealth = attack - Ehealth
      print("Enemy health: " + str(Ehealth))
      
