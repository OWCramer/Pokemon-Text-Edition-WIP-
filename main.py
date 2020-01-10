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
    time.sleep(.5)
    clear()

#defines a fight
def iniate_fight():
  fight_prototype

#Main Title Screen
print ("Welcome to Pokemon Text Edition (Now in Python!)")
screens.screen_title()
print ("")
input('To begin your journey press enter')
clear()
#fake_load()

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
#------------------------------------------------------------------------
iniate_fight()