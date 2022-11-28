import random

besede = ["OPICA", "DINOZAVER", "FAKULTETA", "KROMPIR"] # seznam
beseda = random.choice(besede)

ugibanja = set()
napacna = set()

vislica = [" ", "+--------", "|\n|\n|\n|\n|\n+--------", "+-----------|\n|\n|\n|\n|\n+--------", "+-----------|\n|\n|\n|\n|\n+--------|\n|\n|\n", "+-----------|\n|\n|\n|\n|\n+--------|\n|\n|\nx", "+-----------|\n|\n|\n|\n|\n+--------|\n|\n|\nx|", "+-----------|\n|\n|\n|\n|\n+--------|\n|\n|\nx|/", "+-----------|\n|\n|\n|\n|\n+--------|\n|\n|\nx|/\""] # seznam: postopoma se dodajajo znaki

uganil = False
napaka = 0

while True:
  skrita_beseda = beseda
  print(vislica[napaka])
  print(vislica[len(napacna)]) # število elementov 

  for crka in beseda:
    if crka not in ugibanja:
      skrita_beseda = skrita_beseda.replace(crka, '_')

  if skrita_beseda == beseda:
    break

  print(f"ugani besedo: {skrita_beseda}")
  print("Poskusi si že s črkami: ", ugibanja)
  trenutni_vnos = input("vnesi črko: ")
  trenutni_vnos = trenutni_vnos.capitalize()

  ugibanja.add(trenutni_vnos) # vedno dodamo ne seznam vseh vtipkanih crk.

  if trenutni_vnos not in beseda:
    napacna.add(trenutni_vnos) # če dane črke ni v besedi, jo dodamo med napačne (gre za množico, zato se črke ne podvajajo)

  if len(napacna) >= 6:
    print("konec igre")
    break


