import random

# pobriše terminal
def pobrisi():
  print("\n"*40) # \n = znak za novo vrstico

# funkcija, ki izračuna razliko
def razilka(stevilo1, stevilo2):
  return stevilo1 - stevilo2

rezultat = razilka(100, 20) # calling the function
print(rezultat)


# funkcija, ki izračuna maksimum in izpiše manjšega
def maksimu(st1, st2):
  if st1<st2:
    return st1
  else:
    return st2

z =  float(input("1,število: "))
y = float(input("2, število: "))
maks = maksimu(z,y)
print(maks)


# funkcija, ki izračuna drugi koren števila
def koren(x, k=2):
  return x ** (1/k)

rezultat = koren(64)
print(f"koren števila 64 je {rezultat}")

rezultat2 = koren(64, 3) # vrednost k lahko prepišemo
print(f"kubicni koren števil 64 je {rezultat2}")
    

# glede na vnešene katete s funkcijo izračunamo hipotenuzo
def hipotenuza(kateta1, kateta2):
  return ((kateta1**2 + kateta2**2) ** 0.5)

kateta1 = int(input("prva kateta: "))
kateta2 = int(input("druga kateta: "))
print(f"dolžina hipotenuze {hipotenuza(kateta1, kateta2)}") # calling the function znotraj print

# napredna verzija
def pravilni_tiroktnik(stranica1, stranica2, operacija):
  if operacija == "k":
    return ((stranica1**2 - stranica2**2) ** 0.5)
  elif operacija == "h":
    return ((stranica1**2 + stranica2**2) ** 0.5)

operacija = input("izračun (k)atete ali (h)ipotenuze: ")
if operacija == "h":
  stranica1 = int(input("dolžina katete: "))
else:
  stranica1 = int(input("dolžina hipotenuze: "))

stranica2 = int(input("druga stranica: "))
print(f"rešitev: {pravilni_tiroktnik(stranica1, stranica2, operacija)}")

# še naprednejša verzija
# vedno posredujemo dve števili: k1 in k2 oz. k1/k2 in h
def p_trikotnik(kateta1=0, kateta2=0, hipotenuza=0):
  if kateta2 != 0 and kateta1 == 0 and hipotenuza != 0:
    kateta1 = kateta2 # če posredujemo kateto2 in hipotenuzo, kateto2 preslikamo v kateto1
    kateta2 = 0

  if kateta2 == 0 and kateta2 != 0 and hipotenuza != 0:
    return ((hipotenuza**2)-(kateta1**2))**0.5
  elif kateta1 != 0 and kateta2 != 0 and hipotenuza == 0:
    return ((kateta1**2) + (kateta2**2)) ** 0.5

  if (kateta1 == 0 and kateta2 == 0) or (kateta1 == 0 and hipotenuza == 0) or (kateta2 == 0 and hipotenuza == 0):
    return "izračun ni možen le z 1 parametrom"

k1 = int(input("dolžina katete 1: "))
k2 = int(input("dolžina katete 2: "))
print(f"hipotenuza je: {p_trikotnik(kateta1=k1, kateta2=k2)}")

k = int(input("dolžina katete: "))
h = int(input("dolžina hipotenuze: "))
print(f"druga kateta je: {p_trikotnik(kateta1=k1, hipotenuza=h)}")


# funkcija
def pozdrav(ime, starost):
  print("pozdravljeni {ime}")
  if int(starost) < 18:
    print("premlad si")
  else:
    print("starček")

uporabnik = input("kako ti je ime? ")
starost = input("koliko si star? ")
pozdrav(ime=uporabnik, starost=starost) # tudi če je vrstni red v klicu funkcije drugačen kot pri definiciji same funkcije, ne bo Error


"""
Program združuje vse, kar podpira Python v funkcijah
poleg osnov (posredovanje parametrov, vračanje rezultata)
lahko parametre tudi poimenujemo, pri čemer nam ni treba
posredovati vseh (privzete vrednosti)

Kaj je ARGUMENT in kaj PARAMETER?
Parameter je posrdovana oz. sprejeta stvar V FUNKCIJI
argument je to, kar posredujem noter

(ista stvar z drugega zornega kota)

"""

# asistentova verzija programa
def ptrikotnik(kateta1=0, kateta2=0, hipotenuza=0):
    # tukaj operiram s PARAMETRI (lokalne spremenljivke, ki
    # izhajajo iz sprejetih podatkov) -kateta1, kateta2,
    # hipotenuza

    # POSREDUJEM SI PO DVE:
    # K1, K2 za izračnu hipotenuze
    # Kx, hipotenuza za izračun katete 2

    # če si posredujem hipotenuzo in kateto 2, kateto 2
    # preslikam v kateto 1
    if kateta2 != 0 and kateta1 == 0 and hipotenuza != 0:
        kateta1 = kateta2
        kateta2 = 0

    if kateta2 == 0 and kateta1 != 0 and hipotenuza != 0:
        return ((hipotenuza**2)-(kateta1**2))**0.5

    elif kateta1 != 0 and kateta2 != 0 and hipotenuza == 0:
        return ((kateta1**2)+(kateta2**2))**0.5

    if ((kateta1 == 0 and kateta2 == 0) or
        (kateta1 == 0 and hipotenuza == 0) or
            (kateta2 == 0 and hipotenuza == 0)):
        return "NE MOREM IZRAČUNATI SAMO Z ENIM PARAMETROM"


k1 = int(input("Vnesi kateto 1: "))
k2 = int(input("Vnesi kateto 2: "))

print("Hipozenuza je: ", ptrikotnik(kateta1=k1, kateta2=k2))


h = int(input("Vnesi hipotenuzo: "))
k = int(input("Vnesi kateto: "))

print("Druga kateta je: ", ptrikotnik(kateta1=k, hipotenuza=h))



