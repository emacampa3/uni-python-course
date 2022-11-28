import statistics

slovar = {} # nov slovar

while True:
  ime = input("Vnesi ime: ")

  if ime == "":
    break

  try:
    visina = float(input("Vnesi višino v cm: "))
  except:
    print("Višina mora biti številska, z decimalno piko")
    continue

  slovar[ime] = visina # višina se doda k ključu v slovarju

print(f"Vnesla si {len(slovar)} oseb")
print(slovar)
print(f"Povprecna visina je: {statistics.mean(slovar.values())}")
print(f"Višina najmanjše osebe je: {min(slovar.values())}")
print(f"Višina najvišje osebe je: {max(slovar.values())}")


# na dolgo
najnizji_ime = ""
najnizji_visina = 300
najvisji_ime = ""
najvisji_visina = 0

for kljuc, vrednost in slovar.items():

  if vrednost < najnizji_visina:
    najnizji_ime = kljuc
    najnizji_visina = vrednost

  if vrednost > najvisji_visina:
    najvisji_ime = kljuc
    najvisji_visina = vrednost

print("Najnižja oseba je: ", najnizji_ime)
print("Najvišja oseba je: ", najvisji_ime)

