import sys, pickle # pickle bere binarno, ne tekstovno

def preberi():
  imenik = {}

  try: # ustvarimo imenik
    with open("imenik.pic", "rb") as f:
      imenik = pickle.load(f)
  except:
    print("datoteka je prazna, dodaj kakšen vnos")
  
  return imenik # vrnemo imenik


def shrani():
  try:
    with open("imenik.pic", "wb") as f:
      pickle.dump(imenik, f)
  except:
    konec = input("Ni mi uspelo shraniti, naj vseeno končam program? DA/NE")
    if konec .lower() == "da":
      return True
    else: 
      return False

  return True

def prikaziVse():
  if imenik != {}:
    print("IME".ljust(20, " ") + "TELEFONSKA")
    for ime, telefonska in imenik.items():
      print(f"{ime[:19].title().ljust(20,' ')}\t{telefonska}") # ime izpišemo do 19. znaka
  else:
    print("Preden lahko bereš imenik, moraš vanj kaj zapisati")

  return

# PORAVNAVA
# ljust() in rjust()
# ljust(število-znakov, 'znak, ki nadomesti whitespace') -- ljust(20, ' ')
# metoda title() prvo črko spremeni v veliko

def isciPoImenu():
  ime = input("Vnesi ime: ")
  if ime.lower() in imenik:
    print(f"Telefonska številka: {imenik[ime.lower()]}") 
  else:
    print("Telefonska številka za to ime ne obstaja")

  return


def isciPoTelefonski():
  telefon = input("Vnesi telefonsko: ")
  uspesno = False
  
  for ime, telefonska in imenik.items():
    if telefonska == telefon:
      uspesno = True
      print(f"Telefonska {telefonska} pripada osebi: {ime}")
      break
  if uspesno == False:
    print("Ime za to telefonsko številko ne obstaja")

  return


def dodaj():
  ime = input("Vnesi ime: ")
  telefonska = input("Vnesi telefonsko številko: ")
  imenik[ime.lower()] = telefonska

  return


def popravi():
  ime = input("Vnesi ime: ")
  if ime.lower() in imenik:
    del imenik[ime]
    ime = input("Vnesi novo ime: ")
    telefonska = input("Vnesi novo telefonsko številko: ")
    imenik[ime.lower()] = telefonska
  else:
    print("Ta oseba v imeniku ne obstaja")

  return


def meni():
  while True:
    izbira = input("""
    Kaj želite narediti? 
    1 - PRIKAŽI VSE
    2 - IŠČI PO IMENU
    3 - IŠČI PO TELEFONSKI
    4 - DODAJ
    5 - IZHOD
    izbira: """)

    if izbira == "1":
      prikaziVse()
      continue
    elif izbira == "2":
      isciPoImenu()
      continue
    elif izbira == "3":
      isciPoTelefonski()
      continue
    elif izbira == "4":
      dodaj()
      continue
    elif izbira == "5":
      if shrani == False:
        continue
      else:
        sys.exit(0)
    else:
      print("Neveljavna izbira")

imenik = preberi() # globalni imenik
meni() 
