import os
import datetime
import random

# funkcija, ki vrne število datotek s koncnico ".py" v trenutni mapi
l = os.listdir(".")
print(l)

n = 0

def python(i):
  for i in l:
    if i[-3:] == ".py":
      n += 1
      return n

nPy = n
print(f"v mapi je {n} datotek s končnico .py")


# Zgornjo funkcija: popravljena tako, da se lahko spreminja mapa, v kateri šteje datoteke in končnico, ki se šteje (ima prevzete vrednosti) 
def nFilesEnd(mapa=".", koncnica="py"):
  l = os.listdir(mapa)
  nFiles = 0

  dolzina = len(koncnica) + 1
  for i in l:
    if i[-dolzina:] == "."+koncnica:
      nFiles += 1
  return nFiles


# d = datetime.datetime(2022,1,3) ustvarjen nov datum

# program, ki preveri, ali obstaja mapa z imenom, ki ustreza današnjemu datumu v formatu "LLLL_MM_DD"
d = datetime.datetime.now()
dniz = d.strftime("%Y_%m_%d") # formatiranje datuma

# če mapa ne obstaja, jo ustvari 
if os.path.isdir(dniz):
  print("mapa obstaja")
else: 
  os.mkdir(dniz) # ustvari novo mapo z imenom današnjega datuma v določenem formatu
  print(f"ustvarjena je nova mapa {dniz}")


# funkcija, ki elemente seznama razvrsti v nakljucnem vrstnem redu in vrne nov seznam. Originalni seznam mora ostati nespremenjen.
s = [1,2,3,4,5]
print(random.sample(s,1)) # vrne en element s seznama
print(random.sample(s,5)) # vrne nov seznam 


# funkcija, ki na podlagi dveh podanih datumov izracuna razliko v dnevih. Datuma bosta podana v obliki niza, opcijski argument funkcije pa naj bo tudi format datuma, čigar privzeti format naj bo slovenski zapis datuma (brez presledkov, torej DD.MM.LLLL)
def dnevi(datum1, datum2, formatDatuma="%d.%m.%Y"):
  datum1 = datetime.datetime.strptime(datum1, formatDatuma) # pretvori v objekt tipa datetime
  datum2 = datetime.datetime.strptime(datum2, formatDatuma)

  if datum1 > datum2:
    razlika = datum1 - datum2
  else: 
    razlika = datum2 - datum1

  return razlika.days # dobimo dneve

dnevi("11.04.2000", "29.11.2022") # ne dela!
