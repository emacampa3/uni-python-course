beseda = "DINOZAVER"
ugibanja = ""

while True:
  print(f"dosedanji poskusi: ", ugibanja)
  zac_beseda = beseda

  for crka in zac_beseda:
    if crka not in ugibanja:
      zac_beseda = zac_beseda.replace(crka, '_')

  if zac_beseda == beseda:
    break

  print(f"ugani: {zac_beseda}")
  vtipkana_crka = input("vnesi VELIKO crko: ")
  ugibanja = ugibanja + vtipkana_crka

print("woohoo, uganil si")


print("------\n|    |\n|    O\n|  /-+-/\n|    |\n|    |\n|   | |\n|   | |\n|\n----------\n")


# VISLICE z vnaprej definirano besedo
beseda = "OPICA"
ugibanja = ""
uganil = False

while True:
  skrita_beseda = beseda

  for crka in beseda:
    if crka not in ugibanja:
      skrita_beseda = skrita_beseda.replace(crka, '_')

  print("Ugibaš: ", skrita_beseda)
  print("Poskusil si že s črkami: ", ugibanja)
  trenutni_vnos = input("Vnesi črko: ")
  ugibanja = ugibanja + trenutni_vnos

  if trenutni_vnos in beseda:
    print("Bravo, črka je noter")
