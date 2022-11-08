import random

op = input("Katero operacijo želiš trenirati? 1 - seštevanje; 2 - odštevanje; 3- množenje; 4- deljenje; 5 - naključno: ")
zahtevnost = input ("kako težko želiš? 1-4: ")

if zahtevnost == "1":
  maks = 10
elif zahtevnost == "2":
  maks = 20
elif zahtevnost == "3":
  maks = 50
else:
  maks = 100

vseh = 0
pravilnih = 0

while True:
  # tukaj bo spraševal po številih itd
  
  prvo = random.randint(1, maks)
  drugo = random.randint(1, maks)

  if op == '5':
    operacija = random.randint(1,4)
  else:
    operacija = int(op)

  if operacija == '4' and prvo%drugo!=0:
    continue


  if operacija == 1:
    rezultat = prvo + drugo
    poziv = '+'
  elif operacija == 2:
    rezultat = prvo - drugo
    poziv = '-'
  elif operacija == 3:
    rezultat = prvo * drugo
    poziv = '*'
  else:
    rezultat = prvo / drugo
    poziv = '/'
        

    mnenje = input(f"Izračunaj: {prvo} {poziv} {drugo}: ")

  if mnenje == "x":
    if vseh > 10:
      break
    else:
      print ("Ne moreš še ven!")
      continue
  elif int(mnenje) == rezultat:
    print ("Pravilno!")
    pravilnih+=1
  else:
    print ("Narobe, pravilen rezultat je", rezultat)
          
  vseh+=1

print ("Uspešnost: ", (pravilnih/vseh)*100, '%')

