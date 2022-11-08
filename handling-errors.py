starost = input("bitje, vnesi svojo starost: ")
try: 
  starost = int(starost)
except: # izvede se, če se "try" ne mora izvesti (error)
  print("prosim, vnesi številko")
else: # izvede se samo, če je "try" uspešen
  print(f"staro si {starost} let, bitje")

print("adijo") # izvede se v vsakem primeru


# sprašuje po starosti, dokler ni input integer
while True:
  starost = input("bitje, vnesi svojo starost: ")

  try:
    starost = int(starost)
  except: 
    print("prosim, vnesi številko")
  else: 
    break

print(f"staro si {starost} let, bitje")


# funkcija, ki sprašuje po besedilu, dokler to ni stevilka: uporabno pri večjem številu argumentov
def input_int(besedilo):
  while True:
    stevilka = input(besedilo)

    try:
      stevilka = int(stevilka)
    except:
      print("prosim, vnesi številko")
    else:
      return stevilka

starost = input_int("vnesi starost: ")
visina = input_int("vnesi višino (v cm): ")
masa = input_int("vnesi maso (v kg): ")

print(f"staro si {starost} let, visoko {visina} cm in težko {masa} kg, bitje")

try:
  itm = round(masa/((visina/100)**2), 3)
  print(f"tvoj indeks telesne mase je {itm}")
except ZeroDivisionError: # ujame error pri deljenju z 0
  print("indeksa telesne mase se ne da izračunati, ker je višina 0 cm")
  itm = "N/A"


# float namesto int
def input_float(besedilo):
  while True:
    stevilka = float(besedilo)

    try:
      stevilka = float(stevilka)
    except:
      print("prosim, vnesi številko")
    else:
      return stevilka

starost = input_float("vnesi starost: ")
visina = input_float("vnesi višino: ")
masa = input_float("vnesi maso (v kg): ")

print(f"staro si {starost} let, visoko {visina} cm in težko {masa} kg, bitje")

if visina > 3: # če je vnesel višino v cm, pretvoriš višino v metre
  visina = visina/100
try:
  itm = round(masa/(visina**2), 3)
  print(f"tvoj indeks telesne mase je {itm}")
except ZeroDivisionError:  # ujame error pri deljenju z 0
  print("indeksa telesne mase se ne da izračunati, ker je višina 0 cm")
  itm = "N/A"
