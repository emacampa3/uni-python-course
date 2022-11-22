from math import pi
import copy
import string

ime = input("vnesi svoje ime: ")
print(len(ime))
print(f"druga do četrta črka imena: {ime[2:5]}")

for crka in ime:
  print(crka)

if "a" in ime.lower():
  print("tvoje ime vsebuje a")

# KONTROLA VHODNIH PODATKOV
# prepovedane črke nadomesti z *
ime = input("vnesi svoje ime: ")

prepovedane = "xwyq"

for crka in prepovedane:
  if crka in ime.lower():
    print("v imenu je prepovedana črka")
    ime = ime.replace(crka, "*")
print(f"ime ti je: {ime}")


# če ime vsebuje črke, ki niso del dovoljenih, namesto njih izpiše *
ime = input("vnesi svoje ime: ")

dovoljene = list(string.ascii_letters)

for crka in ime:
  if crka not in dovoljene:
    print(f"v imenu je nedovoljena črka {crka}")
    ime = ime.replace(crka, "*")
print(f"ime ti je: {ime}")


dovoljene = list(string.ascii_letters)
print(dovoljene[2:14:2]) # izpiše števila med 3 in 13, s korakom dva
print(dovoljene[-1:0:-1])  # izpiše števila po vrsti od zadaj
print(dovoljene[4:]) # izpiše od petega znaka naprej
print(dovoljene[4]) # izpiše 5 znak

# izpiše ime od zadaj
ime = input("vnesi svoje ime: ")
print(ime[-1::-1]) 



ime = "Janez"
print(f"{ime^40}")  # poravna ime na sredino 40 vrstic

print(f"{'x':>2} {'x^2':>3} {'x^3':>4}")
for i in range(1, 11):
  print(f"{i:2} {i**2:3} {i**3:4}")

print(f"pi na 5 decimalk natančno je: {pi:.5f}")  # 5 decimalk

for n in range(6):
  # izpiše mesta decimalk za vsa števila med 0 in 6
  print(f"pi na {n} decimalk natančno je: {pi:.{n}f}")


# KOPIRANJE
# dictionary
d = {"a": 1, "b": 2, "c": [1, 2, 3]}

e = d.copy()  # brez uporabe modula: če se spremeni ena vrednost, se spremenita obe, tako kopija kot original
# z uporabo modula: omogoča spremembe samo na e, brez prenosa na  d
e = copy.deepcopy(d)

# slovar
s = [1, 2, 3, 4, ["a", "b"]]
sKaz = s  # sKaz kaze na isto mesto v spominu
sCopy1 = s[:]  # navadno kopiranje brez uporabe modula
sCopy2 = copy.copy(s)  # navadno kopiranje z uporabo modula
sDeepCopy = copy.deepcopy(s)  # popolno kopiranje z uporabo modula



# funkcija, ki preveri, če niz predstavlja binarno število (0 in 1)
def je_dvojisko(niz):
  # niz = niz.strip() odstrani whitespace
  for i in niz:
    if i != "1" and i != "0":
      return False
  return True # če se cela zanka zaključi, brez da bi se returnal false, potem je True


# pretvori iz dvojiškega v desetiškega
def binary2decimal(niz):
  if not je_dvojisko(niz):
    raise Exception("podani niz ni dvojiško število")
  n = len(niz)
  rezultat = 0
  for i in range(n):
    rezultat += int(niz[i])*2**(n - 1 - i)
  return rezultat

# lepša verzija
def binary2decimal2(niz):
  if not je_dvojisko(niz):
    raise Exception("podani niz ni dvojiško število")
  n = len(niz)
  s = list(niz) # spremenimo v seznam in ga obrnemo
  s.reverse()
  rezultat = 0
  for i in range(n):
    rezultat += int(s[i])*2**(i)
  return rezultat


# izpiše število ponovitev določene črke v nizu
def frekvenca(niz):
  frekvenca = {}
  for i in niz:
    if i in frekvenca: # ali ključ obstaja v slovarju
      frekvenca[i] += 1
    else: 
      frekvenca[i] = 1
  return frekvenca


# če je krajši niz vsebovan v daljšem, vrne indekse krajšega v daljšem
def nizi(daljsi, krajsi):
  s = []
  krajsi_dolzina = len(krajsi)
  daljsi_dolzina = len(daljsi)
  for i in range(daljsi_dolzina):
    if daljsi[i:(i + krajsi_dolzina)] == krajsi:
      s.append(i)
  return s

nizi("tralala", "la")

