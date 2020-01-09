#Gets Program and Screens Ready
def title_screen():
  from startup import title_screen
def error_screen():
  from startup import error_screen
import random
import os
import time
from termcolor import colored, cprint
import fight_prototype

#Defines how to clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Main Title Screen
print ("Welcome to Pokemon Text Edition (Now in Python!)")
title_screen()
print ("")
input('To begin your journey press enter')
clear()

'''Professor Dialogue'''
#Professor Startup
print ("Hello,\n Weclome to the Unova Region. I'm professor Aurea Juniper, and I heard you were interested in the world of pokemon! Is that true?(Yes/No)")
while True:
  ready_choice = input(': ')
  ready_choice = ready_choice.lower()
  #Exit Screen
  if ready_choice == 'no':
    clear()
    print ('Fine No Game!')
    error_screen()
    quit()
  elif ready_choice == "yes":
    break
    
  #

#Aurea Juniper Dialougue asks if user wants Pokemon
def do_you_want():
  while True:
    pokemon_own = input(': ')
    pokemon_own = pokemon_own.lower()
    if pokemon_own == 'no':
      clear()
      print ("Well maybe I'll ask another time.")
      error_screen()
      quit()
    elif pokemon_own == 'yes':
      print ('Before we get you a pokemon,')
      break
    else:
      print ("I need a Yes or No answer!")
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
clear()

#continue dialogue 
print ('Nice to meet you ' + name + "!")

#chosing pokemon 
print ("Now that I know your name you can choose a pokemon!")
pokemon_list = []
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


#Meeting rival
print ("Hey im undefined ")
