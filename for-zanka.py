list(range(3)) # [0,1,2]
list(range(1, 10, 2))  # [1,3,5,7,9] tretja vrednost je "korak"
list(range(5, 0, -1))  # [5, 4, 3, 2, 1]


n = 10
for i in range(0, n+1):  # od 1 do n
  print(i)

for i in range(n, -1, -1):  # od n do 0
  print(i)


# izračun zmnožka naravnih števil od 1 do vnešenega števila
n = int(input("Vnesi naravno število: "))
ponovitve = 1 # štetje ponovitev
for i in range(1, n+1): # od 1 do n (range začne pri 0)
    ponovitve = ponovitve * i
print(f"Zmnožek vseh naravnih števil med 1 in {n} = {ponovitve}")

# seštevek potenc realnega števila: x = realno število (x**0 + x**1 + x**2 + ... + x**n)
realno_stevilo = float(input("realno število: "))
naravno_stevilo = int(input("naravno število: "))

vsota = 0

for i in range(0, naravno_stevilo + 1): # vključno z naravnim_stevilom
  vsota = round(vsota + realno_stevilo ** i, 2)
print(vsota)


# izračun fakultete
naravno_stevilo = int(input("naravno število: "))
zmnožek = 1
for i in range(1, naravno_stevilo + 1):
  zmnožek *= i # množiš z i: vsa števila med 1 in naravno_stevilo
print(zmnožek)


# vsota kompliciranih členov
realno_stevilo = float(input("realno število: "))
naravno_stevilo = int(input("naravno število: "))

vsota = 0

for i in range(1, naravno_stevilo + 1):
  vsota = vsota + (-1)**(i+1) * realno_stevilo**i / i
print(vsota)

# vsota kompliciranih členov z while zanko
vsota = 0

i = 1  # i se začne pri 0
while i <= n:  # zadnji izračun bo pri i = n
  vsota = vsota + (-1)**(i+1) * realno_stevilo**i / i
  i += 1  # i povečamo za 1
print(vsota)


# seštevamo naravna števila po vrsti, dokler ni vsota >= danemu številu
stevilo = float(input("celo pozitivno število: "))
vsota = 0
zacetna_vrednost = 0 # ena manj, kot prvi člen

while vsota < stevilo:
  zacetna_vrednost += 1 # povečamo za 1
  vsota += zacetna_vrednost # prištejemo k vsoti
print(f"da dosežemo vsaj vsoto {stevilo}, moramo sešteti vsaj {zacetna_vrednost} naravnih števil")


# kvadrat iz zvezdic: NE DELA PRAV!
dolzina_stranice = int(input("dolžina stranice: "))
sirina_roba = 0

while sirina_roba < 1:
  sirina_roba = int(input("širina roba: ")) # vprašaj za širino, dokler ne izpolnjuje pogoja 

for i in range(dolzina_stranice):
  for j in range(dolzina_stranice):
    if i < sirina_roba or i > (dolzina_stranice - sirina_roba - 1) or j < sirina_roba or j > (dolzina_stranice - sirina_roba - 1):
      print("* ", end="")
    else: #če ni rob, je prazno
      print(" ", end="")
  print() #skok v novo vrstico


# diamant iz zvezdic: REŠI!
