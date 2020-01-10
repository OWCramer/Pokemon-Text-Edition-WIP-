''' fight prototype'''
import random
import os
from random import randint
from main import name
from main import pokemon_list_rival
from main import pokemon_list
  TF = True
  def clear():
      os.system('cls' if os.name=='nt' else 'clear')
  class Rival_pokemon_B1():
      global pokemon_list_rival
      def __init__(self, BaseHP = 20):
          self.name = pokemon_list_rival[0]
          self.Lv = 5
          self.move_one = "Scratch"
          self.move_one_attack = 7
          self.move_two = "Growl"
          self.move_two_attack = 0
          self.BaseHP = BaseHP
          MoveCC = 100
          MoveMC = MoveCC * 2
          self.HP = 50

      #(C)haracter (P)okemon (S)lot
  class CPS1():
      def __init__(self, BaseHP = 50):
          self.BaseHP = BaseHP
          self.Lv = 5
          self.name = pokemon_list[0]
          self.HP = 0.02 * self.Lv * self.BaseHP * 10
          MoveCC = 20
          MoveMC = MoveCC * 2
          EPNeeded = 10
          self.EP = 0.0
          self.move_one = "Tackle"
          self.move_one_attack = 10
          self.move_one_CC = 40
          self.move_two = "Growl"
          self.move_two_attack = 0
          self.move_two_CC = 40
          self.move_three = "Empty"
          self.move_three_attack = 0
          self.move_three_CC = 40
          self.move_four = "Empty"
          self.move_four_attack = 0
          self.move_four_CC = 40
          self.EP = 0.0
          self.EPNeeded = 10
  RB = Rival_pokemon_B1()
  CB = CPS1()         
  misschance = random.randint(1,80)
  if misschance == 26:
    misschanceBool = True
  else:
    misschanceBool = False
  critchance = random.randint(1,40)
  if critchance == 7:
    critchanceBool = True
  else:
    critchanceBool = False
  def Player_fight_prompt():
      global TF
      moveSelectOption = input(": ").capitalize()
      clear()
      print()
      if moveSelectOption == CB.move_one:
          TF = False
          print(CB.name + " used " + CB.move_one)
          if misschanceBool == True:
              print ("Attack Missed")
          else:
              if critchanceBool == True:
                  CB.move_one_attack = CB.move_one_attack * 2
                  RB.HP = RB.HP - CB.move_one_attack
                  CB.move_one_attack = CB.move_one_attack / 2
                  print("Critical hit")
              else:
                  RB.HP = RB.HP - CB.move_one_attack
                  print("Attack hit")
      elif moveSelectOption == CB.move_two:
          TF = False
          print(CB.name + " used " + CB.move_two)
          if misschanceBool == True:
              print ("Attack Missed")
          else:
              if critchanceBool == True:
                  CB.move_two_attack = CB.move_two_attack * 2
                  RB.HP = RB.HP - CB.move_two_attack
                  CB.move_two_attack = CB.move_two_attack / 2
                  print("Critical hit")
              else:
                  RB.HP = RB.HP - CB.move_two_attack
                  print("Attack hit")
      elif moveSelectOption == CB.move_three:
          TF = False
          print(CB.name + " used " + CB.move_three)
          if misschanceBool == True:
              print ("Attack Missed")
          else:
              if critchanceBool == True:
                  CB.move_three_attack = CB.move_three_attack * 2
                  RB.HP = RB.HP - CB.move_three_attack
                  CB.move_three_attack = CB.move_three_attack / 2
                  print("Critical hit")
              else:
                  RB.HP = RB.HP - CB.move_three_attack
                  print("Attack hit")
      elif moveSelectOption == CB.move_four:
          TF = False
          print(CB.name + " used " + CB.move_four)
          if misschanceBool == True:
              print ("Attack Missed")
          else:
              if critchanceBool == True:
                  CB.move_four_attack = CB.move_four_attack * 2
                  RB.HP = RB.HP - CB.move_four_attack
                  CB.move_four_attack = CB.move_four
              else:
                  RB.HP = RB.HP - CB.move_four_attack
                  print("Attack hit")
      elif moveSelectOption == "Back":
          attack_while_loop()
      else:
          print ("Thats not an option! (Type Back)")
          return Player_fight_prompt()
  print (name + ": Go, " + CB.name + ".")
  print ("Rival: Sent out, " + RB.name + ".")
  print ()
  qwert = input("Press Enter To Continue...")
  clear()
  def attack_while_loop():
      while(RB.HP > 0):
          print ()
          print ("Rival:             " + name + ":")
          print (RB.name + " Lv." + str(RB.Lv) + "         " + CB.name + " Lv." + str(CB.Lv))
          print ("HP: " + str(RB.HP) + "             " + "HP: " + str(round(CB.HP)))
          print ()
          print ("[Fight] [Bag] [Run] [Pokemon]")
          print ("-----------------------------")
          OptionUI = input(": ").lower()
          if CB.move_two == "Empty":
              CB.move_two = " "
          if CB.move_three == "Empty":
              CB.move_three = " "
          if CB.move_four == "Empty":
              CB.move_four = " "
          if OptionUI == "fight":
              print(CB.move_one + "      " + CB.move_two)
              print(CB.move_three + "       " + CB.move_four)
              print("      Back")
          if CB.move_two == " ":
              CB.move_two = "Empty"
          if CB.move_three == " ":
              CB.move_three = "Empty"
          if CB.move_four == " ":
              CB.move_four = "Empty"
          Player_fight_prompt()
          print()
          Enemy_attack_option = random.randint(1,3)
          if Enemy_attack_option < 3:
              print ("Rival's " + RB.name + " used " + RB.move_one)
              CB.HP = CB.HP - RB.move_one_attack
              print ("Attack hit")
          else:
              print("Rival's " + RB.name + " used " + RB.move_two)
              CB.HP = CB.HP - RB.move_two_attack
              print ("Attack hit")
          if OptionUI == "bag":
            print()
            print("You dont have anything in there yet!")
            attack_while_loop()
          if OptionUI == "run":
            print()
            print("You cant run from trainer Battles!")
            attack_while_loop()
          if OptionUI == "pokemon":
            print()
            print("You only have one pokemon!")
            attack_while_loop()
  attack_while_loop()
  print("You gained 17 XP for defeating " + RB.name)
  CB.EP = CB.EP + 17
  if CB.EP >= CB.EPNeeded:
    CB.Lv = CB.Lv + 1
    CB.EP = CB.EP - CB.EPNeeded
    CB.EPNeeded = CB.EPNeeded * .5
    print(CB.name + " leveled up to Lv." + str(CB.Lv) + "!")
    print("You need " + CB.EP - CB.EPNeeded + "XP to level up again!")

