from funkcija import input_float
from itm_funkcija import itm, presodi_itm

starost = input_float("vnesi starost: ")
visina = input_float("vnesi višino: ")
masa = input_float("vnesi maso (v kg): ")

itm = itm(masa, visina)

print(f"staro si {starost} let, visoko {visina} cm in težko {masa} kg, bitje")

if visina > 3:
  visina = visina/100
try:
  itm = round(masa/(visina**2), 3)
  print(f"tvoj indeks telesne mase je {itm}, kar pomeni {presodi_itm}")
except ZeroDivisionError:
  print("indeksa telesne mase se ne da izračunati, ker je višina 0 cm")
  itm = "N/A"
