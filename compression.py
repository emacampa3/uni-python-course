import sys, os

# sprašuje po mapi, če obstaja, vstopim vanjo in grem ven
def izbor_mape():
  while True:
    izbor = input("vnesi mapo, kjer so fotografije, ali Q za izhod: ")
    if izbor.upper() == "Q":
      sys.exit()
    
    try:
      os.chdir(izbor) # vstopi v mapo
      return izbor
    except: 
      print("mapa ne obstaja")

seznam_slik = []

def pregled_datotek(mapa):
  vse_datoteke = os.listdir(mapa)
  print(vse_datoteke)

  # če se konča na jp(e)g, doda na nov seznam
  for datoteka in vse_datoteke:
    if datoteka.lower().endswith(".jpg") or datoteka.lower().endswith(".jpeg"):
      seznam_slik.append(datoteka)
  
  return seznam_slik

# če je seznam prazen, quit
if len(seznam_slik):
  print("mapa ne vsebuje fotk")
  sys.exit()

mapa = izbor_mape()
fotografije = pregled_datotek(mapa)
print(fotografije)


# for datoteka in fotografije:
#   os.system("convert -resize 800x800" + mapa + datoteka + " " + mapa + datoteka + "mini.jpg")

# download ImageMagick: končni produkt: python program zmanjša velikost vseh slik v mapi (ne morem dowloadati na macu)
# terminal: convert -resize VELIKOSTxVELIKOST ime_datoteke mini.jpg
