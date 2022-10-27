# primer zahtevnejše zanke:
while True:
  n = input("Vnesite število med 2 in 20. Za konec pritistnite samo ENTER. Vnos: ")
  if n == "":
    break
  n = int(n)
  if n < 2 or n > 20:
    continue
  for i in range(1, n+1):
    for j in range(1, i+1):
      if j < 10:
        print(0, end="")
    print(j, end=" ")
  print()

# izpiše števila med 1 in 10
i = 1
while i <= 10:
  print(i)
  i += 1


# vpraša za ime, dokler input ni prazen
ime = input("Vnestite ime: ")
while ime: # dokler ime ni prazen niz
  print("Pozdravljen ", ime, "!", sep="")
  ime = input("Vnestite ime: ")


# program brez while zanke
stevilo = 23
a = int(input("ugibaj: "))
n = 0
maxPoskusov = 5

while a != stevilo and n <= maxPoskusov:  # prekini, ko je število poskusov večje od 5
  if a < stevilo:
    print(f"vneseno število je premajhno")
  else:
    print(f"vneseno število je preveliko")
  if n < maxPoskusov:
    # vprašaj za input samo, ko je število poskusov manjše od maxPoskusov
    a = int(input("ugibaj: "))
  n += 1

if a == stevilo:
  print(f"Uganil si v {n}-tem poskusu")


# poenostavljen zgornji program z while zanko
x = 23
n = 0

while True:
  a = int(input("ugibaj: "))
  n += 1
  if a == x:
    print(f"uganil si v {n}-tem poskusu")
    break
  elif a > x:
    print(f"število je preveliko")
  else:
    print(f"število je premajhno")


# sprašuje po številu, dokler ni input prazen, nato poda maximum izmed vseh vnešenih števil
stevilo = input("vnesi število: ")
maksimum = float(stevilo)

while stevilo:
  stevilo = input("vnesi število: ")
  if stevilo == "":  # če je empty string, se zanka konča
    break
  stevilo = float(stevilo)
  if stevilo > maksimum:
    maksimum = stevilo

print(f"največje vneseno število je {maksimum}")


# preveri, ali je vneseno število pozitivno
while True:
  n = int(input("Vnesi pozitivno število: "))
  if n > 0:
    break
  else:
    print("Število ni pozitivno")

i = n
while i > 0:
  if i % 3 == 0:
    print("pozor")  # če je število deljivo s 3, ga pri izpisu nadomesti z "pozor"
  else:
    print(i)  # sicer izpiši število
  i -= 1  # od n do 0
print("zdaj")

# izpiši števila po vrsti do n
i = 0
while i <= n:
  print(i)
  i += 1
