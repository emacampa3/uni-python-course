predmeti = {}
predmeti["UvP"] = {"prof": "AŽ", "ime": "Uvod v programiranje"}
predmeti["DIP"] = {"prof": "EP", "ime": "Družboslovno-informatični praktikum"}
predmeti["Ang"] = {"prof": "MS", "ime": "Strokovna angleščina"}
predmeti["SocOrg"] = {"prof": "AR", "ime": "Sociologija organizacij"}

for seznam in sorted(predmeti.keys()): # izpiši seznam ključev
  print(seznam)

while True:
  kljuc = input("vnesi ključ predmeta: ")
  if kljuc in predmeti:
    print(predmeti[kljuc]["prof"].upper() + " je nosilec pri predmetu:" + predmeti[kljuc]["ime"].upper())
  else:
    break


