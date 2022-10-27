# random računanje
print(5, "+", 4, "=", 5+4) # izpis računa

max(3, 5, 6) # razvrsti elemente po velikosti
max("a", "b")  # male črke bližje koncu abecede so "večje"

# 3e5 = 3x10**5 = 300000

a = "5"
a*4  # result = aaaa

int(a) + 4  # result = 9
a*4  # result = 16

teža = int(input("Koliko tehtate? "))
print(teža)

petStr = "5" # string
petInt = int(petStr) # integer
petFloat = float(petStr) # float

1/(4**2)
(2**0 + 2**1 + 2**3 + 2**4)**(1/3)

# logični operatorji: če želimo, da je program vrne True, ko je vsaj en izmed vseh False: negiramo vse skupaj, vmes je OR, ali pa negiramo vsako posebaj in je vsem AND

# če je sodo število, vrne True
x = 9
if x % 2 == 0:
  True

# če je število deljivo z 7, vrne True
x = 9
if x % 7 == 0:
  True


# program, ki v outputu zamenja dani vrednosti spremenljivk
a = input("a: ")
b = input("b: ")

c = b  # v tretjo spremenljivko začasno shranimo vrednost b
b = a
a = c

print(f"a: {a}; b: {b}")
