imeDatoteke = "datoteka.txt"

def pisi():
  ime = input("vnesi svoje ime: ")
  with open(imeDatoteke, "a") as f:  # append: dodaja imena, a brez ločila/nove vrstice
    f.write(ime + "\n")  # vsak input da v novo vrstico
  return

def izpis():
  try:
    with open(imeDatoteke, "r") as vf:
      print(vf.read())
  except: 
    print("preden lahko bereš, moraš kaj zapisati")

  return

while True:
  print(f"""Izberi:
  - 1 za pisanje imen
  - 2 za izpis imen
  - 3 za izhod
  """)

  izbira = input("vpiši eno izmed črk: ")

  if izbira == "1":
    pisi()
    continue
  elif izbira == "2":
    izpis()
    continue
  elif izbira == "3":
    break
  else:
    print("napačna izbira")
    continue
    

    


