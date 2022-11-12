import string

ime = input("vnesi svoje ime: ")
print(len(ime))
print(f"druga do četrta črka imena: {ime[2:5]}")

for crka in ime:
  print(crka)

if "a" in ime.lower():
  print("tvoje ime vsebuje a")

# KONTROLA VHODNIH PODATKOV
# prepovedane črke nadomesti z *
ime = input("vnesi svoje ime: ")

prepovedane = "xwyq"

for crka in prepovedane:
  if crka in ime.lower():
    print("v imenu je prepovedana črka")
    ime = ime.replace(crka, "*")
print(f"ime ti je: {ime}")


# če ime vsebuje črke, ki niso del dovoljenih, namesto njih izpiše *
ime = input("vnesi svoje ime: ")

dovoljene = list(string.ascii_letters)

for crka in ime:
  if crka not in dovoljene:
    print(f"v imenu je nedovoljena črka {crka}")
    ime = ime.replace(crka, "*")
print(f"ime ti je: {ime}")


dovoljene = list(string.ascii_letters)
print(dovoljene[2:14:2]) # izpiše števila med 3 in 13, s korakom dva
print(dovoljene[-1:0:-1])  # izpiše števila po vrsti od zadaj
print(dovoljene[4:]) # izpiše od petega znaka naprej
print(dovoljene[4]) # izpiše 5 znak

# izpiše ime od zadaj
ime = input("vnesi svoje ime: ")
print(ime[-1::-1]) 

