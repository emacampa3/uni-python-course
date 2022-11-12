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

print("woohoo, uganu si")
