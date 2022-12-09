import random

# izračun števila pi
def razdalja(x, y):
  return ((x**2) + (y**2)) ** 0.5

notri = 0
vse = 1000000 # določa natančnosti števila pi: več kot jih je, bolj natančen je rezultat

for a in range(0, vse): # 10000x se ponovi
  x = random.random() # vrne naključno število med 0 in 1
  y = random.random() 

  if razdalja (x,y) <= 1: # znotraj krogra
    notri += 1

print(f"vseh točk: {vse}, notri jih je {notri}")

pi = (4*notri)/vse

print(f"pi po mojem znaša {pi}")
