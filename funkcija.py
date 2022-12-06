import random
import time

# funkcija, ki generira n celih števil na intervalu [1, k] in jih vrne v obliki seznama. k mora biti argument funkcije ()celo število, vecje od 1)
def generiranjeŠtevil(n, k):
  if type(k) != type(1): # preverimo, če je celo število
    raise Exception("K ni celo število")
  if k <= 1:
    raise Exception("K mora biti večji od 1")
  
  s = []
  for i in range(n):
    s.append(random.randint(1,k))
  return s

# calling the function
seznam = generiranjeŠtevil(10,10)
print(seznam)


# ključi iz slovarja: list(f.keys())
# list(f.items()) dobiš seznam, kjer je prva stvar ključ, druga pa vrednost
# če to sortiramo, ga sortira po vrednostih ključa

# funkcija, ki ta seznam sprejme kot argument in izracuna frekvenčno tabelo (kolikokrat se vsako število ponovi)
# NE DELA!
def izpisiFrekvenco(seznam, uredi=False, padajoce=False):
  tabela = list(seznam.items())

  def izberiDruga(x):
    return x[1]

  if uredi == "frekvenca":
    tabela.sort(keys=izberiDruga, reverse=padajoce)
  elif uredi == "vrednost":
    tabela.sort(reverse=padajoce)
  
  print("vrednost | frekvenca")
  print("---------+----------")
  for i in tabela:
    print(f"{i[0]:<5}| {i[1]}")


izpisiFrekvenco(seznam)

# za funkcijo izmerite, koliko ˇčasa potrebuje, če generirate 100, 1000, 10000 in 100000 celih števil iz intervala[1, 5]. Podatke izpišite na zaslon v obliki tabele
ns = [100, 1000, 10000, 100000]
casi = []
for n in ns: 
  t1 = time.time()
  x = generiranjeŠtevil(n,5)
  t2 = time.time()
  casi.append(t2 -t1)
