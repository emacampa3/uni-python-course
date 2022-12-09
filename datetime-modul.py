from datetime import datetime

danes = datetime.now()

# sprašuje po rojstvu, dokler ni oblika zapisa prava
while True:
  datum_rojstva = input("vnesi datum rojstva v formatu LLLL-mm-dd: ") # to je string
  try:
    # strptime: pretvori besedilo v čas (povemo kaj pretvarjamo in v kakšnem formatu)
    datum_rojstva = datetime.strptime(datum_rojstva, "%Y-%m-%d")
  except: 
    print("vnesi datum v ustrezni obliki")
    continue
  break

starost = (danes - datum_rojstva).days

print(f"starost: {starost} dni oz. {int(starost/365)} let")
# round: zaokroži, int: prepiše samo celoštevilski del, "zaokroži navzdol"


# druga verzija, kjer so inputi ločeni
danes = datetime.now()

while True:
  leto_rojstva = input("vnesi leto rojstva: ")
  mesec_rojstva = input("vnesi mesec rojstva: ")
  dan_rojstva = input("vnesi dan rojstva: ")
  try:
    datum_rojstva = datetime.strptime(leto_rojstva + "-" + mesec_rojstva + "-" + dan_rojstva, "%Y-%m-%d")
  except:
    print("vnesi datum rojstva v ustrezni obliki")
    continue
  break

starost = (danes - datum_rojstva).days

print(f"starost: {starost} dni oz. {int(starost/365)} let")


# tretja verzija, kjer je računanje starosti optimalno
leto_rojstva = input("vnesi leto rojstva: ")
mesec_rojstva = input("vnesi mesec rojstva: ")
dan_rojstva = input("vnesi dan rojstva: ")

# trenutni čas
danes = datetime.now()
# strftime: pretvori datum v string (kaj pretvarjamo in v kakšno obliko)
danes_leto = datetime.strftime(danes, "%Y") # dobimo leto kot besedilo
danes_mmdd = datetime.strftime(danes, "%m%d") # dobimo mesec in dan kot besedilo 

starost = int(danes_leto) - int(leto_rojstva) - 1
rojen_mmdd = int(mesec_rojstva + dan_rojstva)

if int(danes_mmdd) > rojen_mmdd: 
  starost += 1

print(f"starost: {starost} let")
