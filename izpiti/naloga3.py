# Napišite funkcijo, ki sprejme seznam števil, ki predstavlja nek vektor, in ime ciljne datoteke. Funkcija mora ta seznam zapisati v Pajkovo datoteko s končnico ”.vec”. Format Pajkove datoteke za vektorje(.vec) je: v prvi vrstici je besedilo ”* Vertices n ”, kjer n predstavlja število enot/vrednosti. Nato je vsaki vrstici navedena ena vrednost.
# Primer Pajkove datoteke za vektorje za seznam z vrednostmi 1, 2 in 3:
# * Vertices 3
# 1
# 2
# 3
# Krierajte tudi en seznam števil in ga s pomočjo vaše funkcije zapišite v datoteko.

def funkcija(seznam, datoteka):
  n = len(seznam)
  with open(datoteka, "w") as f:
    f.write(f"* Vertices {n}\n")
    for i in seznam:
      f.write(f"{i}\n")

seznam = [2,3,4,5,6]

funkcija(seznam, "seznam.vec") # ustvari nov file

