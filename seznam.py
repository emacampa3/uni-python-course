znamke = []

for ponovitev in range(1, 6):
  vnos = input("Vnesi znamke vozila: ")

  znamke.append(vnos)

# shranimo vnose, kopiramo cel seznam
znamke_prej = znamke[:]
# spreminjamo original
del (znamke[0])
# pogledamo, kaj je v seznamih
print(znamke)
print(znamke_prej)
