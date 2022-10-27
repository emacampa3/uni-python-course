# pijača na osebo
ime = input("Vpiši svoje ime: ")
pijaca = float(input("Koliko litrov pijače imate: "))  # realno število
osebe = int(input("Koliko ljudi jo bo pilo: "))  # celo število

pijacaNaOsebo = pijaca/osebe

print(ime, "je kupil/a", pijaca, "litrov pijace in povabil/a", osebe, "oseb")
print("To pomeni, da pride na osebo", pijacaNaOsebo, "litrov pijace")

if (pijacaNaOsebo > 1):
  print(3*"Hura! ")
else:
  print("B" + 20*"U" + "!")
