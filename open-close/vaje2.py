import os

imeDatoteke = "datoteka.txt"

def pisi():
  ime = input("vnesi svoje ime: ")
  with open(imeDatoteke, "a") as f:  # append: dodaja imena, a brez ločila/nove vrstice
    f.write(ime + "\n")  # vsak input da v novo vrstico
  
  return

def izpis():
  try:
    n = 1
    with open(imeDatoteke, "r") as datoteka:
      vrstica = datoteka.readline()  # preberemo prvo vrstico
      while len(vrstica) != 0: # dokler nismo na koncu datoteke
        print(str(n) + " - " + vrstica, end="")
        vrstica = datoteka.readline()  # preberemo naslednjo vrstico
        n += 1
  except: 
    print("preden lahko bereš, moraš kaj zapisati")
  return

def brisanje(): # beremo vrstico po vrstico, dodajamo na seznam
  vsebinaDatoteke = []
  print("v datoteki imaš: ")
  izpis() # izpiše vse kar je v datoteki

  while True:
    try:
      vrstaZaIzbris = int(input("katero vrstico naj izbrišem: "))
      break
    except: 
      print("vnesi številko vrstice")
      continue

  try:
    n = 1
    with open(imeDatoteke, "r") as datoteka:
      vrstica = datoteka.readline()
      while len(vrstica) != 0:
        if n != vrstaZaIzbris:
          vsebinaDatoteke.append(vrstica)
        vrstica = datoteka.readline()
        n += 1
  except:
    print("ničesar ni za brisati")
    return # ne nadaljuje
  
  print("v seznamu je zdaj: ")
  print(vsebinaDatoteke)
 
  os.remove(imeDatoteke) # izbrišemo prejšnjo datoteko, da se vsebina ne podvoji

  with open(imeDatoteke, "a") as datoteka:
    for vrsta in vsebinaDatoteke:
      datoteka.write(vrsta)

  print("izbrisano, nova vsebina: ")
  izpis()
  return

while True:
  print(f"""Izberi:
  - 1 za pisanje imen
  - 2 za izpis imen
  - 3 za brisanje vnosa
  - 4 za izhod
  """)

  izbira = input("vpiši eno izmed števil: ")

  if izbira == "1":
    pisi()
    continue
  elif izbira == "2":
    izpis()
    continue
  elif izbira == "3":
    brisanje()
    continue
  elif izbira == "4":
    break
  else:
    print("napačna izbira")
    continue
    

    


