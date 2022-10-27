a = float(input("vpiši število: "))
b = float(input("vpiši število: "))

print(f"vsota vpisanih števil je {a+b}")


# obseg in ploščina kvadrata
a = float(input("Stranica kvadrata: "))
print(f"obseg kvadrata: {a*4}; ploščina kvadrata: {a**2}")


# izračun končnega (zaokroženega) zneska z obrestno mero čez določeno obdobje
znesek = float(input("znesek: "))
r = float(input("obrestna mera v odstotkih: "))
n = int(input("število let: "))

x = round(znesek/(1 + (r/100)**n), 2)
print(f"{znesek} evrov bo čez {n} let, pri obrestni meri {r}%, vredno {x} evrov")


# pretvarjanje merskih enot
mera = input("vpišite 1 ali 2: 1 pomeni pretvorbo iz inčev v cm, 2 pa iz cm v inče: ")
dolzina = float(input("število za pretvorbo: "))

if (mera == "1"):
  print(f"{dolzina} inčev je {dolzina * 2.54} cm")
else:
  print(f"{dolzina} cm je {dolzina//2.54} inčev")


# je število sodo ali liho?
stevilo = int(input("Vnesite poljubno število: "))

if stevilo % 2 == 0:
  print(f"Število {stevilo} je sodo")
else:
  print(f"Število {stevilo} je liho")


# ali je prvo število delitelj drugega?
a = int(input("Število 1: "))
b = int(input("Število 2: "))

if a % b == 0:
  print(f"Število {a} je deljitelj števila {b}")
else:
  print(f"Število {a} ni deljitelj števila {b}")


# glede na vnešene katete izračunamo hipotenuzo
a = int(input("Kateta 1: "))
b = int(input("Kateta 2: "))

c = ((a*a + b*b) ** 0.5) # Pitagorov izrek
print(f"vpisani kateti {a} in {b} določata hipotenuzo dolžine {c}")


# deljenje
stevilo1 = float(input("Prvo število: "))
stevilo2 = float(input("Drugo število: "))
rezultat = stevilo1//stevilo2
print(f"{stevilo1} deljeno z {stevilo2} je {rezultat}")
# print(stevilo1, " deljeno z", stevilo2, " je ", rezultat, ".") drugačen zapis


# Vpišite 3 števila in preverite, ali so to možne dolžine stranic v trikotniku (trikotniška neenakost): če je dolžina dveh stranic krajša od dolžine tretje, trikotnika ne moremo sestaviti
a = float(input("Število 1: "))
b = float(input("Število 2: "))
c = float(input("Število 3: "))

# če je en pogoj znotraj oklepaja izpoljnjen, stranice ne morejo sestavljati trikotnika
if (a+b < c or b+c < a or a+c < b):
  print(f"vpisana števila {a}, {b} in {c} ne morajo bit dolžine stranic v trikotniku")
else:
  print(f"vpisana števila {a}, {b} in {c} so lahko dolžine stranic v trikotniku")



# Heronova formula: S = pod korenom: s*(s-a)*(s-b)*(s-c), pri čemer je s = (a+b+c)/2
print(f"izračun ploščine trikotnika")
a = float(input("prva stranica: "))
b = float(input("druga stranica: "))
c = float(input("tretja stranica: "))

# če je dolžina dveh stranic krajša od dolžine tretje, trikotnika ne moremo sestaviti in tudi ne izračunati ploščine
if (a+b < c or b+c < a or a+c < b):
  print(f"ploščine se ne da izračunati")
else:
  s = (a + b + c)/2
  p = round((s*(s-a)*(s-b)*(s-c))**(1/2), 2)

  print(f"ploščina trikotnika je {p}")


# izračun fakulteta vnesenega števila
n = int(input("vnesi število: "))
f = 1
nIzpis = n  # shranimo vrednost

while n > 1:
  f = f*n
  n -= 1
print(f"fakulteta števila {nIzpis} = {f}")

# 2. način za izračun fakulteta vnesenega števila
vnos = int(input("vnesi število: "))
stevec = 1
rezultat = n  # shranimo vrednost

while stevec <= vnos:
  rezultat *= stevec
  stevec += 1
print(f"fakulteta števila {vnos} = {rezultat}")
