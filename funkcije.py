
# pobriše terminal
def pobrisi():
  print("\n"*40) # \n = znak za novo vrstico

# funkcija, ki izračuna razliko
def razilka(stevilo1, stevilo2):
  return stevilo1 - stevilo2

rezultat = razilka(100, 20) # calling the function
print(rezultat)

# funkcija, ki izračuna maksimum in izpiše manjšega
def maksimu(st1, st2):
  if st1<st2:
    return st1
  else:
    return st2


z =  float(input("1,število: "))
y = float(input("2, število: "))
maks = maksimu(z,y)
print(maks)

# funkcija, ki izračuna drugi koren števila
def koren(x, k=2):
  return x ** (1/k)

rezultat = koren(64)
print(f"koren števila 64 je {rezultat}")

rezultat2 = koren(64, 3) # vrednost k lahko prepišemo
print(f"kubicni koren števil 64 je {rezultat2}")
    

