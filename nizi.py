# ord("a") # dobimo ASCII število 97
# chr(97) # dobimo črko "a"

# računa ujemanje dveh imen (glede na mesto v abecedi)
ime1 = input("vnesi prvo ime: ")
ime2 = input("vnesi drugo ime: ")

vsota = 0
crke = "abcčdefghijklmoprsštuvzž"

for crka in (ime1 + ime2): 
  if crka.lower() in crke:
    vsota += int(crke.index(crka)) + 1
    
    # če je vsota večja od 100, seštejemo prvi dve števili in dodamo število na 3. mestu
    if vsota > 100: 
      pretvorjeno = str(vsota)
      sestevek = str(int(pretvorjeno[0]) + int(pretvorjeno[1])) + pretvorjeno[2]

print(f"odstotek ujemanja: {sestevek} %")


# a[0] izpiše prvi znak
# a[-1] izpiše zadnji znak
# a[-2] izpiše predzadnji znak
# a[:-1] izpiše cel niz, razen zadnjega znaka
# type(int(vnos)) == type(1) preveri, če je vnos lahko integer


# program, ki iz a = "Dober dan!" in b = "Janko, kako si danes?" sestavi niz "Dober dan, Janko!"
a = "Dober dan!"
b = "Janko, kako si danes?"
print(a[:-1] + b[5:7] + b[:5] + a[-1])


# Zakrij črke: funkcija, ki sprejme dva niza, vrne prvega in vse znake, ki se pojavljajo tudi v drugem nizu, zamenja z znakom "#"

prviNiz = input("vnesi niz: ")
drugiNiz = input("vnesi drugi niz: ")
noviNiz = "" # prazen niz

# gre čez vse črke v prvem nizu, če je ta črka tudi v drugem nizu, jo nadomesti z "#", sicer jo prepiše v noviNiz
for crka in prviNiz:
  if crka in drugiNiz:
    noviNiz += "#"
  else:
    noviNiz += crka

print(noviNiz)


# Kontrolna številka: funkcija, ki sprejme niz; niz mora preveriti, ali je to veljavna koda za nek obrazec. Pogoji za veljavno kodo so: dolžina je natanko 11 znakov, vsi znaki so številke, ostanek pri deljenju seštevka prvi 10-tih števil mora biti enak 11-ti števki
def kontrola(stevilo):
  if len(stevilo) != 11:
    return False
  try:
    n = 0
    for i in stevilo[:-1]: # gre čez cel niz, razen zadnjega znaka
      n = n + int(i) # sešteva števke
    if n%10 == int(stevilo[-1]):
      return True
    else: 
      return False
  except:
    return False

stevilo = input("vnesi niz: ")

funkcija = kontrola(stevilo)
print(funkcija)


# Izpis za vislice: funkcija, ki sprejme dva niza: vrne prvi niz, kjer vse znake, ki NISO navedeni v drugem nizu in niso ločila ali presledki zamenja z podčrtaji "_". Poleg tega naj vrne tudi število znakov, ki so bili zamenjani. Ker rezultat sestavljen iz dveh delov, naj ga vrne v obliki slovarja, kot ključe naj uporabi beseda in število
# NE ZNAM VRNITI V OBLIKI SLOVARJA
def vislice(niz1, niz2):
  noviNiz = "" # prazen niz
  stZamenjanih = 0
  # slovar = {}
  for znak in niz1.lower():
    if znak not in niz2.lower(): 
      noviNiz += znak
    else:
      noviNiz += "_"
      stZamenjanih += 1
  
  return stZamenjanih, noviNiz
      
niz1 = input("vnesi niz: ")
niz2 = input("vnesi še en niz: ")

funkcija = vislice(niz1, niz2)
print(funkcija)


# Razdalja2D: Napišite funkcijo, ki po formuli izračuna evklidsko razdaljo med dvema točkama v dvorazsežnem prostoru, ki sta podani kot dva seznama ali n-terki dolžine 2
def razdalja(a, b):
  # spremeni seznam z str v seznam z int, seznamA.split() pa iz vnosa naredi seznam, kjer so elementi ločeni tam, kjer je pri vnosu presledek
  a = list(map(int, seznamA.split()))
  b = list(map(int, seznamB.split()))
  return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)

# input je vedno izven funkcije
seznamA = input("vnesi dve števili: ")
seznamB = input("vnesi dve števili: ")

funkcija = razdalja(seznamA, seznamB)
print(funkcija)


# Razdalja: nadgrajena zgornja funkcija, ki deluje v poljubno razsežnem prostoru, torej kjer so točke definirane z poljubno dolgimi seznami ali n-terkami (obe morata biti enake dolžine)
def razdalja(a, b):
  a = list(map(int, seznamA.split()))
  b = list(map(int, seznamB.split()))
  
  if len(a) != len(b):
    raise Exception("oba seznama morata biti iste dolžine")
  
  d = 0
  for i in range(len(a)):
    d = d + (a[i] - b[i] ** 2)
  
  return d ** (1/2)

seznamA = input("vnesi števila: ")
seznamB = input("vnesi števila: ")

funkcija = razdalja(seznamA, seznamB)
print(funkcija)


# Preštej: Napišite funkcijo, ki sprejme kot argument seznam in še en objekt. Funkcija naj prešteje, koliko izmed elementov seznama je enakih drugemu elementu
# NE DELA!
def prestej(seznam, objekt):
  n = 0
  for i in seznam:
    if i == objekt:
      n += 1
  return n

seznam = list(input("vnesi seznam: "))
objekt = input("vnesi objekt: ")

funkcija = prestej(seznam, objekt)
print(funkcija)


# Preštej int: funkcija, ki sprejme kot argument seznam in prešteje, koliko izmed elementov je razreda int
# NE DELA!
def funkcija(seznam):
  n = 0
  for i in seznam:
    if type(i) == type(1):
      n = n + 1
  return n

seznam = list(input("vnesi seznam: "))

klic = funkcija(seznam)
print(klic)
