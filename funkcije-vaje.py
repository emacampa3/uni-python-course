import math

# kvadrat števila
def kvadrat(stevilo):
  rezultat = stevilo**2
  return rezultat

print(kvadrat(10))


# potenca
def potenca(x, p=2):
  rezultat = x**p
  return rezultat

print(potenca(2,3)) # potenca je podana 2**3
print(potenca(2)) # 2**2

# koren
def koren(stevilo):
  if stevilo > 0:
    return math.sqrt(stevilo)
  else:
    return "pod korenom mora biti pozitivno število"

koreni = koren(25)
print(koreni)


# matematični izraz
def mat(n,x): # parametri funkcije
  rezultat = 0
  for i in range(1, n+1): # gre do n
    rezultat = rezultat + (-1)**(i+1) * x**(-i)
    return rezultat 

račun = mat(2,10) # vhodni podatki podani preko argumentov 
print(račun)

# je vnešen input lahko število ali ne?: 
def stevilo(x):
  try:
    float(x)
    return True
  except: 
    return False

print(stevilo(10)) # True
print(stevilo("bla")) # False
print(stevilo(1/2)) # True
