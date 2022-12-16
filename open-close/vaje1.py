# input vpiše v novo datoteko
ime = input ("Prosim, vnesi ime: ")

with open ('datoteka.txt', "w") as datoteka:
  datoteka.write(ime)
    

# program, ki se ponavlja, sprašuje za vnos števila, ki določa funkcionalnost
ime_datoteke = "datoteka.txt"

# izpiše že vpisana imena v datoteki
# def izpis():
#   with open(ime_datoteke, "r") as datoteka:
#     vsebina_datoteke = datoteka.read()
#     print(vsebina_datoteke)

#   return

# drugačna verzija zgornje funkcije izpis(): oštevilčni vsako vrstico
def izpis():
  with open(ime_datoteke, "r") as datoteka:
    vrstica = datoteka.readline()
    while len(vrstica) != 0:
      print(vrstica, end='')
      vrstica = datoteka.readline()

  return

# def vpis():
#   ime = input("Prosim, vnesi ime: ")
#   with open(ime_datoteke, "w") as datoteka:
#     datoteka.write(ime)
#   return

# boljša verzija zgornje funkcije vpis() z uporabo append
def vpis():
  ime = input("Prosim, vnesi ime: ")
  with open(ime_datoteke, "a") as datoteka:
    datoteka.write(ime + '\n') # doda novo vrstico
  
  return

while True:
  izbira = input("""
Izberi funkcionalnost: \n
1 - izpis vsebine datoteke
2 - pisanje v datoteko
3 - izhod     \n
Kaj boš izbrala:                
""")

  if izbira == "1":
    izpis()
    continue
  elif izbira == "2":
    vpis()
    continue
  elif izbira == "3":
    break
  else:
    print("Napačen vnos, poskusi znova...")
    continue
