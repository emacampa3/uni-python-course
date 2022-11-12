from funkcije import deljenje, mnozenje, odstevanje, sestevanje

dovoljene_operacije = "+-*/"
minimum = 0
maksimum = 0
aritmeticna_sredina = 0

vsota = 0
deljitelj = 0

zanka1 = True
zanka2 = True
zanka3 = True

while zanka1:
  while True:
    print(f"""
    izberi:

    K za kalkulator
    S za statistike
    I za izhod 
    """)
    izbira = input("vpiši eno izmed naštetih možnosti: ")

    if izbira.upper() == "K":
      print()
      zanka2 = True
      break
    elif izbira.upper() == "I":
      print("konec programa")
      print(f"minimum = {minimum} \nmaksimum = {maksimum} \naritmetična sredina = {aritmeticna_sredina}")
      quit()
    elif izbira.upper() == "S":
      print(f"minimum = {minimum}, \nmaksimum = {maksimum}, \naritmetična sredina = {aritmeticna_sredina}")
      quit()
    else:
      print("neveljaven vnos")
      continue
    
  try: 
    rezultat = float(input("število:   "))
  
    if rezultat < minimum:
      minimum = rezultat
      maksimum = minimum
    elif rezultat > maksimum:
      maksimum = rezultat
      minimum = maksimum

      deljitelj += 1
      vsota += rezultat

    while zanka2:
      operacija = input("operacija: ")
      if operacija.upper() == "Q":
        zanka2 = False
        continue

      if operacija not in dovoljene_operacije:
        print("neveljaven vnos")
        continue

      while zanka3:
        stevilo = input("število:   ")
        if stevilo.upper() == "Q":
          zanka2 = False
          break
        elif type(float(stevilo)) != float:
          print("neveljaven vnos")
          continue
        else:
          stevilo = float(stevilo)
          break
 
      if operacija == "+":
        rezultat = sestevanje(rezultat, stevilo)
      elif operacija == "-":
        rezultat = odstevanje(rezultat, stevilo)
      elif operacija == "*":
        rezultat = mnozenje(rezultat, stevilo)
      elif operacija == "/":
        rezultat = deljenje(rezultat, stevilo)
      
      if stevilo < minimum:
        minimum = stevilo
      elif stevilo > maksimum:
        maksimum = stevilo
      
      deljitelj += 1
      vsota += stevilo
      aritmeticna_sredina = round(vsota / deljitelj, 2)
      
      print(f"rezultat = {rezultat}")
    
  except: 
    print("neveljaven vnos")
    continue

# napaka, ki je ne znam rešiti, je sledeča: če user v zanki3 oz. pri inputu za število vnese "q", program sicer pravilno izkoči iz zanke, in nadaljuje po pričakovanjih, vendar se hkrati izpiše zadnji except stavek "neveljaven vnos"
