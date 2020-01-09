''' fight prototype'''
import pokemon_moves
import random
from random import randint

class Enemy_poke():
  def Level():
    print ("Lv.5")
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
  
class Poke():
  def Level():
    level = 5
    print ("Lv." + str(level))
  def name():
    print ("test_name")
  def Moves():
    move_list = [move1(), move2(), move3(), move4()]
  def move1():
    print ("AT1")
    attack = 10
  def move2():
    print ("AT2")
    attack = 15
  def move3():
    print ("AT3")
    attack = 20
  def move4():
    print ("AT4")
    attack = 25
  def Health():
    health = 50
misschance = random.randint(1,50)
if misschance == 26:
  misschanceBool = True
else:
  misschanceBool = False
critchance = random.randint(1,20)
if critchance == 7:
  critchanceBool = True
else:
  critchanceBool = False
def fight():
  Ehealth = 0
  #global Enemy_poke_name_here.Health()
  global move_list
  #global Ehealth
  Enemy_poke_name.Health()
  poke_name_here.Health()
  print(Enemy_poke.Name() + " "+ Enemy_poke.Level())
  print("HP: " + str(Ehealth))
  print ()
  print(poke.Name() + " " + poke.Level())
  print("HP: " + str(health))
  print()
  print("[Fight] [Run] [Bag] [Pokemon]")
  option1 = input(": ").lower()
  if option1 == "fight":
    print (move_list)
    if option1 == "AT1" and misschanceBool == True:
      poke.move1()
      if critchanceBool == True:
        print ("critical hit")
        attack = attack *2
      Ehealth = attack - Ehealth
      print("Enemy health: " + str(Ehealth))
      print ("Your health: " + str(health))
      print("attack hit!")
    else:
      print ("Attack missed")
  
      
