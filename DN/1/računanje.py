import random

while True:
  izbira_operacije = input(f"""
  RAČUNSKE NALOGE

  + za seštevanje
  - za odštevanje
  * za množenje
  / za deljenje
  ? za mešano
  x za izhod

  vpiši eno izmed naštetih možnosti: """)

  if izbira_operacije == "x":
    print("konec programa")
    quit()
  elif izbira_operacije != "+" and izbira_operacije != "-" and izbira_operacije != "*" and izbira_operacije != "/" and izbira_operacije != "?":
    print()
    print("vpiši eno izmed veljavnih možnosti")
    continue
  else:
    break
  
izbira_zahtevnosti = int(input(f"""
izbira zahtevnosti nalog:

1 - operatorji do 10
2 - operatorji do 25
3 - operatorji do 100
4 - operatorji do 1000

vpiši eno izmed števil 1 in 4: """))

stevilo_ponovitev = 0
stevilo_uspesnih_rezultatov = 0

while True:

  if izbira_zahtevnosti == 1:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
  elif izbira_zahtevnosti == 2:
    x = random.randint(1, 25)
    y = random.randint(1, 25)
  elif izbira_zahtevnosti == 3:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
  elif izbira_zahtevnosti == 4:
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
  else: 
    print("vpiši eno izmed števil 1, 2, 3 ali 4")

  # seštevanje
  if izbira_operacije == "+":
    z = x + y
    ugibanje = input(f"{x} + {y} = ")

    if ugibanje == "x":
      if stevilo_ponovitev >= 10:
        break
      else:
        print("za izhod iz programa je potrebno rešiti vsaj 10 računov")
        continue
    else:
      resitev = int(ugibanje)

    # na žalost se ta del kode 3x ponovi, poskusila sem ga dati ven iz tega if stavka, da je identacija enaka kot za prvi ugnezdeni if, vendar tako ta del kode deluje le za seštevanje in množenje, pri odštevanju pa nekaj "zašteka" in se računi večkrat ponovijo, hkrati pa ne izpiše ali je rešitev pravilna oz. napačna
    # bom vesela kakšnega nasveta, kako se da to izboljšati

    if resitev == z:
      print(f"pravilno!")
      stevilo_ponovitev += 1
      stevilo_uspesnih_rezultatov += 1
      continue
    else:
      print(f"napačno, prava rešitev: {x} + {y} = {z}")
      stevilo_ponovitev += 1
      continue

  # odštevanje
  if izbira_operacije == "-":
    if (x > y):
      z = x - y
      ugibanje = input(f"{x} - {y} = ")

      if ugibanje == "x":
        if stevilo_ponovitev >= 10:
          break
        else:
          print("za izhod iz programa je potrebno rešiti vsaj 10 računov")
          continue
      else:
        resitev = int(ugibanje)
      
      if resitev == z:
        print(f"pravilno!")
        stevilo_ponovitev += 1
        stevilo_uspesnih_rezultatov += 1
        continue
      else:
        print(f"napačno, prava rešitev: {x} - {y} = {z}")
        stevilo_ponovitev += 1
        continue

  # množenje
  if izbira_operacije == "*":
    z = x * y
    ugibanje = input(f"{x} * {y} = ")

    if ugibanje == "x":
      if stevilo_ponovitev >= 10:
        break
      else:
        print("za izhod iz programa je potrebno rešiti vsaj 10 računov")
        continue
    else:
      resitev = int(ugibanje)
    
    if resitev == z:
      print(f"pravilno!")
      stevilo_ponovitev += 1
      stevilo_uspesnih_rezultatov += 1
      continue
    else:
      print(f"napačno, prava rešitev: {x} * {y} = {z}")
      stevilo_ponovitev += 1
      continue

  # deljenje
  if izbira_operacije == "/":
    if (x % y) == 0 and (x > y) and y != 1:
      z = x / y
      ugibanje = input(f"{x} / {y} = ")

      if ugibanje == "x":
        if stevilo_ponovitev >= 10:
          break
        else:
          print("za izhod iz programa je potrebno rešiti vsaj 10 računov")
          continue
      else:
        resitev = int(ugibanje)

      if resitev == z:
        print(f"pravilno!")
        stevilo_ponovitev += 1
        stevilo_uspesnih_rezultatov += 1
        continue
      else:
        print(f"napačno, prava rešitev: {x} / {y} = {z}")
        stevilo_ponovitev += 1
        continue

  # mešano
  if izbira_operacije == "?":
    operator = random.choice(["+", "-", "*", "/"])
    
    if operator == "+":
      z = x + y
    elif operator == "-":
      z = x - y
    elif operator == "*":
      z = x * y
    elif operator == "/":  # program redkeje poda deljenje, saj gre čez le, če x in y ustrezata pogojem
      if (x % y) == 0 and (x > y) and y != 1:  
        z = x / y
      else:
        continue
    
    ugibanje = input(f"{x} {operator} {y} = ")

    if ugibanje == "x":
      if stevilo_ponovitev >= 10:
        break
      else:
        print("za izhod iz programa je potrebno rešiti vsaj 10 računov")
        continue
    else:
      resitev = int(ugibanje)

    if resitev == z:
      print(f"pravilno!")
      stevilo_ponovitev += 1
      stevilo_uspesnih_rezultatov += 1
      continue
    else:
      print(f"napačno, prava rešitev: {x} {operator} {y} = {z}")
      stevilo_ponovitev += 1
      continue


uspeh = round(float(stevilo_uspesnih_rezultatov/stevilo_ponovitev)*100,2)

print(f"pravilno je bilo rešenih {stevilo_uspesnih_rezultatov} računov od skupno {stevilo_ponovitev}: uspeh {uspeh} %")

