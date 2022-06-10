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
  print(f"Er zijn nog {lucifers} lucifers")  
  a = int(input("Hoeveel lucifers wil je trekken? "))    
  
  # check ofinput tussen 1 en 3 is
  if a < 1 or a > 3:
    print("Je mag maximaal 3 lucifers trekken!")
    continue  

  lucifers -= a
  if lucifers <= 0:
    print(f"Je hebt verloren {naam} :(!")
    active = False
    continue
    
  b = random.randint(1, 3)
  lucifers -= b
  print(f"De computer pakt {b} lucifer(s)")  

  if lucifers <= 0:
    print(f"Je hebt gewonnen {naam} :)!")
    active = False
    continue

    # spel afgelopen    
    active = False    


print()

   
