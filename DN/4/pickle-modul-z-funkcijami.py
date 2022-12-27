import pickle

try:
  with open("imenik.pic", "rb") as f:
    imenik = pickle.load(f)
except:
  imenik = {}

imeDatoteke = "python/DN/4/imenik-DN.pic"

def dodaj():
  with open(imeDatoteke, "a") as f:
      ime = input("Vnesi ime: ")
      telefonska = input("Vnesi telefonsko številko: ")
      imenik[ime] = telefonska
      f.write(ime + ": " + telefonska + "\n")
  
  return


def isci():
  ime = input("Vnesi ime: ")
  with open(imeDatoteke, "r") as f:
    if ime in imenik:
      print(f"Telefonska številka: {imenik[ime]}")
    else:
      print("Telefonska številka za to ime ne obstaja")

  return


def prikaziVse():
  if imenik != {}:
    for ime, telefonska in imenik.items():
      print(f"{ime}: {telefonska}")
  else:
    print("Preden lahko bereš imenik, moraš vanj kaj zapisati")
  
  return


def popravi():
  ime = input("Vnesi ime: ")
  with open(imeDatoteke, "w") as f:
      if ime in imenik:
        del imenik[ime]
        ime = input("Vnesi novo ime: ")
        telefonska = input("Vnesi novo telefonsko številko: ")
        imenik[ime] = telefonska
      else:
        print("Ta oseba v imeniku ne obstaja")
  
  return


def brisi():
  ime = input("Vnesi ime: ")
  with open(imeDatoteke, "w") as f:
    if ime in imenik:
      del imenik[ime]
      print(f"Iz imenika je bila izbrisana oseba: {ime}")
    else:
      print("Telefonska številka za izbrano ime ne obstaja")
  
  return


while True:
  izbira = input("""
  Kaj želite narediti? 
  1 - DODAJ
  2 - IŠČI
  3 - PRIKAŽI VSE
  4 - POPRAVI
  5 - BRIŠI
  I - IZHOD
  izbira: """)

  if izbira == "1":
    dodaj()
    continue
  elif izbira == "2":
    isci()
    continue
  elif izbira == "3":
    prikaziVse()
    continue
  elif izbira == "4":
    popravi()
    continue
  elif izbira == "5":
    brisi()
    continue
  elif izbira.upper() == "I":
    break
  else:
    print("Neveljavna izbira")

with open("imenik.pic", "wb") as f:
  pickle.dump(imenik, f)
