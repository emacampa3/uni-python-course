import random

besede = ["OPICA", "DINOZAVER", "FAKULTETA", "KROMPIR"]
beseda = random.choice(besede)

ugibanja = ""

uganil = False
napaka = 0

while True:
  print(f"dosedanji poskusi: ", ugibanja)
  skrita_beseda = beseda

  for crka in beseda:
    if crka not in ugibanja:
      skrita_beseda = skrita_beseda.replace(crka, '_')

  if skrita_beseda == beseda:
    break

  print(f"ugani: {skrita_beseda}")
  print(f"poskusil si že črke: {ugibanja}")
  trenutni_vnos = input("Vnesi črko: ")
  ugibanja = ugibanja + trenutni_vnos

  if trenutni_vnos in beseda:
    print("Bravo, črka je noter")
  else: 
    napaka += 1
  
  if napaka == 10:
    print("konec igre")
    print("------\n|    |\n|    O\n|  /-+-/\n|    |\n|    |\n|   | |\n|   | |\n|\n----------\n")
