from math import pi

# samostojen program: je modul

def krog(r):
  return round(pi * r ** 2, 2)

def pravokotnik(a, b=-1):
  if b == -1:
    b = a
  return a*b

def trikotnik(a, b, c):
  s = (a + b + c)/2
  return (s * (s - a) * (s - b) * (s - c))**(1/2)

def main():
  while True:
    izbira = input("""
    ploščino katerega lika bi izračunal? 
    k - krog, p - pravokotnik, t - trikotnik, i - izhod
    izbira: """)

    if izbira == "k":
      r = float(input("polmer kroga: "))
      print(f"ploščina kroga = {krog(r)}")
    elif izbira == "p":
      a = float(input("vnesite prvo stranico: "))
      b = float(input("vnesite drugo stranico: "))
      print(f"ploščina pravokotnika = {pravokotnik(a,b)}")
    elif izbira == "t":
      a = float(input("vnesite prvo stranico: "))
      b = float(input("vnesite drugo stranico: "))
      c = float(input("vnesite tretjo stranico: "))
      print(f"ploščina trikotnika = {trikotnik(a, b, c)}")
    elif izbira == "i":
      break
    else:
      print("neveljavna izbira")

# funkcija main() se izvede samo če zaženemo main program
if __name__ == "__main__":
  main()
