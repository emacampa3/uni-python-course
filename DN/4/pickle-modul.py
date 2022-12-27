import pickle

try:
  with open("imenik.pic", "rb") as f: 
    imenik = pickle.load(f)
except:
  imenik = {}

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
    ime = input("Vnesi ime: ")
    telefonska = input("Vnesi telefonsko številko: ")
    imenik[ime] = telefonska
  elif izbira == "2":
    ime = input("Vnesi ime: ")
    if ime in imenik:
      print(f"Telefonska številka: {imenik[ime]}")
    else:
      print("Telefonska številka za to ime ne obstaja")
  elif izbira == "3":
    for ime, telefonska in imenik.items():
      print(f"{ime}: {telefonska}")
  elif izbira == "4":
    ime = input("Vnesi ime: ")
    if ime in imenik: 
      del imenik[ime]
      ime = input("Vnesi novo ime: ")
      telefonska = input("Vnesi novo telefonsko številko: ")
      imenik[ime] = telefonska
    else: 
      print("Ta oseba v imeniku ne obstaja")
  elif izbira == "5":
    ime = input("Vnesi ime: ")
    if ime in imenik:
      del imenik[ime]
    else:
      print("Telefonska številka za to ime ne obstaja")
  elif izbira.upper() == "I":
    break
  else:
    print("Neveljavna izbira")

with open("imenik.pic", "wb") as f:
  pickle.dump(imenik, f)
