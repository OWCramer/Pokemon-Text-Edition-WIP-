#Different scenarios ex. visiting the pokemon ConnectionError

def pokemon_center():
  print ("Hello im nurse Joy!")
  while True:
    heal_choice = input("Do you want me to heal your Pokemon?(Yes/No): ")
    heal_choice = heal_choice.lower
    if heal_choice == 'yes':
      break
    elif heal_choice == 'no':
      break
    else:
      print ("I need a Yes or No answer!")
      continue

def error():
  print ("\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a")