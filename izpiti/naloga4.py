# Napišite program, ki bo 1000-krat simuliral poskus dobiti 6 pri metanju kocke (torej slučajni izbor številke med 1 in 6), s tem da so vsakič na voljo 3 poskusi. Program naj na koncu izpiše, kolikokrat (izmed 1000 poskusov) je bil za 6 dovolj 1 met, kolikorat 2, kolikorat 3 in kolikokrat v 3 poskusih ni bila vržena šestica. Izpis naj bo v obliki tabele, na primer takole (vrednosti so izmišljene, oblika je lahko tudi drugačna, le da bo ”lepa”):
# Met  | Frekvenca
# -----+----------
# 1    | 152
# 2    | 143
# 3    | 111
# -    | 594

import random

def funkcija():
  for i in range(1,4): # i gre od 1 do 3
    x = random.randint(1,6)
    if x == 6:
      return i
      break # funkcija se zaključi, če je kadarkoli v treh metih rezultat 6, sicer gre čez to zanko, do drugega return statementa z minusom
  return "-"

# nov slovar
seznam = {1:0, 2:0, 3:0, "-":0} # vse vrednosti so na začetku 0, nato samo dodajamo števila
for i in range(1000):
  poskus = funkcija() # kličemo funkcijo: vrne število 1, 2, 3 ali pa "-"
  seznam[poskus] += 1 # prištejemo 1 ob ustreznem ključu

# izpis v terminalu
print("Met | Frekvenca")
for k in [1,2,3,"-"]:
  print(f"{k}   | {seznam[k]:3}")
