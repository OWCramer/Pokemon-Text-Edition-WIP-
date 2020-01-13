#Gets Program and Screens Ready
import screens
import random
import os
import time
from termcolor import colored, cprint
import sprites
import scenarios

#Defines how to clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#defines a loading bar
def fake_load():
  load_bar = "="
  x = 20
  for i in range(21):
    end_cap = " "*x
    print ("Loading...")
    print ("[" + load_bar + end_cap + ']')
    x = x - 1
    load_bar = load_bar + "="
    time.sleep(.1)
    clear()

#Main Title Screen
print ("Welcome to Pokemon Text Edition (Now in Python!)")
screens.screen_title()
print ("")
input('To begin your journey press enter')
clear()
fake_load()

'''Professor Dialogue'''
#Professor Startup
print ("Hello,\n Weclome to the Unova Region. I'm professor Aurea Juniper, and I heard you were interested in the world of pokemon!")
while True:
  print("Is that true?(Yes/No)")
  ready_choice = input(': ')
  ready_choice = ready_choice.lower()
  #Exit Screen
  if ready_choice == 'no':
    clear()
    print ('Fine No Game!')
    screens.screen_error()
    quit()
  elif ready_choice == "yes":
    break
  else:
    print("I need a Yes/No answer")
    scenarios.error()
    continue

#Aurea Juniper Dialougue asks if user wants Pokemon
def do_you_want():
  while True:
    pokemon_own = input(': ')
    pokemon_own = pokemon_own.lower()
    if pokemon_own == 'no':
      clear()
      print ("Well maybe I'll ask another time.")
      screens.screen_error()
      quit()
    elif pokemon_own == 'yes':
      print ('Before we get you a pokemon,')
      break
    else:
      print ("I need a Yes or No answer!")
      scenarios.error()
      print ("Did you want a Pokemon?")

print ("That's great to hear. I'm excited to help you begin your adventure.")
while True:
  print ("Have you ever seen a Pokemon (Yes/No)")
  seen_pokemon = input(': ')
  seen_pokemon = seen_pokemon.lower()
  if seen_pokemon == "yes":
    print ("Thats wonderful, I noticed that you don't have a pokemon of youre own. Would you like one?(Yes/No)")
    do_you_want()
    break
  elif seen_pokemon == "no":
    print ("Oh! Well then how would you like a pokemon of your own?(Yes/No)")
    do_you_want()
    break
  else:
    print ("I need a Yes or No answer!")
    scenarios.error()
    continue

#gets users Name
while True:
  print ('what is your name?')
  name = str(input(': '))
  print ("So your name is " + name + " ? (Yes/No)")

  confirm = input(': ')
  confirm = confirm.lower()
  if confirm == 'no':
    continue
  elif confirm == 'yes':
    break
  else:
    print ("I need a Yes or No answer!")
    scenarios.error()
clear()

#continue dialogue 
print ('Nice to meet you ' + name + "!")

#chosing pokemon 
print ("Now that I know your name you can choose a pokemon!")
pokemon_list = []
pokemon_list_rival = []
pokemon_list_pc = []
while True:
  print ('Which pokemon would you like to choose?(Snivy/Oshawott/Tepig)')
  pokemon_choice = input(": ")
  pokemon_choice = pokemon_choice.lower()
  if pokemon_choice == 'snivy':
    are_you_sure = input('Are you sure you want Snivy?(Yes/No): ')
    are_you_sure=are_you_sure.lower()
    if are_you_sure == 'yes':
      cprint('You chose Snivy', "green")
      pokemon_list.append("Snivy")
      pokemon_list_rival.append("Oshawott")
      time.sleep(1.5)
      input("Press Enter to continue")
      clear()
      break
    elif are_you_sure == 'no':
      continue
    else:
      print ("I need a Yes or No Answer")
      continue
  if pokemon_choice == 'oshawott':
    are_you_sure = input('Are you sure you want Oshawott?(Yes/No): ')
    are_you_sure=are_you_sure.lower()
    if are_you_sure == 'yes':
      cprint('You chose Oshawott', "blue")
      pokemon_list.append("Oshawott")
      pokemon_list_rival.append("Tepig")
      time.sleep(1.5)
      input("Press Enter to continue")
      clear()
      break
    elif are_you_sure == 'no':
      continue
    else:
      print ("I need a Yes or No Answer")
      continue
  if pokemon_choice == 'tepig':
    are_you_sure = input('Are you sure you want Tepig?(Yes/No): ')
    are_you_sure=are_you_sure.lower()
    if are_you_sure == 'yes':
      cprint('You chose Tepig', "red")
      pokemon_list.append("Tepig")
      pokemon_list_rival.append("Snivy")
      time.sleep(1.5)
      input("Press Enter to continue")
      clear()
      break
    elif are_you_sure == 'no':
      continue
    else:
      print ("I need a Yes or No Answer")
      continue
  else:
    print ("Please Check the Spelling of the PKMN name you typed!")
    scenarios.error()
#Meeting rival
sprites.rival()
rival_name = ("Silver")
print ("Hey im your rival Silver!\nI got my first Pokemon today to! Lets Battle!")
time.sleep(1.5)
input("Press enter to continue.")
clear()
fake_load()
#Starts fight
def rival_fight():
  TF = True
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

rival_fight()
#ends fight
#Continues Story
clear()
print ("Thanks for playing this is a WIP")
