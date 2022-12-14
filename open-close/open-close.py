# "odpremo" datoteko za pisanje, če ta ne obstaja, jo program sam ustvari (v isti mapi, kot je .py file)
f = open("prvaDatoteka.txt", "w")
f.write("""To je prva datoteka,
ki smo jo napisali s Pythonom""")
f.close()

# odpremo prvo datoteko za branje, text izpišeš in ga izpišeš na terminalu
f2 = open("prvaDatoteka.txt", "r")
txt = f2.read()
f2.close()
print(txt)

# odpiranje datoteke: f = open("ime_dat", opcija): opcija je lahko BRANJE "r", PISANJE "w", DODAJANJE na koncu "a" (append)

# BRANJE PO VRSTICAH: f.readline() vrne seznam, kjer vsak element predstavlja svojo vrstico

# BOLJŠA VERZIJA: odpre datoteko, kar naredimo se shrani v f, datoteka pa se po koncu pisanja samodejno zapre
with open("prvadatoteka.txt", "w") as f:
  f.write("to je prva datoteka")

# še ena verzija: izpiše vsebino datoteke po vrsticah, ki jih oštevilči
# for zanka gre čez odprt objekt za branje
f2 = open("prvaDatoteka.txt", "r") # read
index = 0
for vrstica in f2:
  index += 1
  print(f"{index}: {vrstica}") # pisanje v terminal, ne piše teksta v novo datoteko
f2.close()

# branje datoteke z for zanko
f = open("prvaDatoteka.txt")
for line in f: # iterira čez vse vrstice
  print(line, end="") # vsako vrstico izpiše posebej
f.close()
    

# open/close z funkcijo
def kopirajDatoteko(vhodnaDat, izhodnaDat):
  with open(vhodnaDat, "r") as vhodniFile:
    vsebina = vhodniFile.read() # preberemo in shranimo v spremenljivko "vsebina"
  with open(izhodnaDat, "w") as izhodniFile: # odpremo, v izhodniFile shranimo vsebino in zapremo
    izhodniFile.write(vsebina)

# ustvarimo dve novi datoteki, kjer je druga le kopija prve z drugim imenom: v terminalu izpiše None, a pravilno ustvari dve datoteki (združitev s prvim zapisom, ki ustvari prvaDatoteka.txt)
kopiranje = kopirajDatoteko("prvaDatoteka.txt", "izhodnaDatoteka.txt")


# boljša verzija: krajši zapis brez dodatne spremenljivke
def kopirajdatoteko2(vhodnaDat, izhodnaDat):
  with open(vhodnaDat, "r") as fileVhodna: # za branje odpreš vhodni file
    with open(izhodnaDat, "w") as izhodniFile: # za pisanje odpreš izhodni file
      izhodniFile.write(fileVhodna.read()) # v izhodni file napišeš to, kar prebereš v vhodnem filu
