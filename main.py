import random

active = True
r = range(1, 4)

print ("Welkom bij Lucifer game")
print()

naam = input ('Vul hier je naam in: ')
print()

print ("Je speelt tegen een computer die een getal kiest tussen 20 en 25, om de beurt trekt een speler 1,2 of 3 lucifers weg. De speler die het laatste lucifer trekt,verliest!!!" )

lucifers = random.randint(20, 25)
print()

while active:
  a = int(input("Hoeveel lucifers wil je trekken? "))
  if a in r:
    print(lucifers)
    print(a)
    lucifers -= a
    print(lucifers)
  
    if lucifers <= 0:
      print("verloren")
      gewonnen = False
      active = False
    if lucifers > 0:
      b = random.randint(1, 3)
      print(lucifers)
      print(b)
      lucifers -= b
      print(lucifers)
    if lucifers <= 0:
      print("gewonnen")
      gewonnen = True
      active = False
  else:
    print("Je mag maximaal 3 lucifers trekken!")


if gewonnen:
  print("YEEEEEH GEWONNEN")
if not gewonnen:
  print("Je hebt verloren!")
  
  
   
