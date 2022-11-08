from math import pi

# del program.py
def krog(r):
  return round(pi * r ** 2, 2)

def pravokotnik(a, b = -1):
  if b == -1:
    b = a
  return a*b

def trikotnik(a, b, c):
  s = (a + b + c)/2
  tmp = s * (s - a) * (s - b) * (s - c)
  if tmp < 0:
    raise Exception("stranice ne morejo sestaviti trikotnika")
  return (tmp)**(1/2)

