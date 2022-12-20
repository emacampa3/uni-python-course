import pickle

try:
  with open("imenik.pic", "rb") as f: # preberemo, če datoteka obstaja
    imenik = pickle.load(f)
except:
  imenik = {}

while True:
  izbira = input("kaj želite narediti? 1 - vnos tel., 2 - izpis tel., 3 - izbris tel., k - konec: izbira: ")
  if izbira == "1":
    ime = input("vnesi ime: ")
    tel = input("vnesi tel: ")
    imenik[ime] = tel
  elif izbira == "2":
    ime = input("vnesi ime: ")
    if ime in imenik:
      print(imenik[ime]) # izpišemo telefonsko
    else:
      print("tel za to ime ne obstaja")
  elif izbira == "3":
    ime = input("vnesi ime: ")
    if ime in imenik:
      del imenik[ime]
    else:
      print("tel za to ime ne obstaja")
  elif izbira == "k":
    break
  else:
    print("neveljavna izbira")

# shranimo, da daluje tudi po zaprtju
with open("imenik.pic", "wb") as f:
  pickle.dump(imenik, f)
