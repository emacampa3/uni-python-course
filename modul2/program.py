from funkcije import krog, pravokotnik, trikotnik

# sprašuje po izračunu lika, dokler user ne vpiše "i" za izhod
while True:
  izbira = input("""
  ploščino katerega lika bi izračunal? 
  k - krog, p - pravokotnik, t - trikotnik, i - izhod
  izbira: """)
  
  try:
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
  
  except:
    print("neveljaven vnos")

