import random, time
# igra iskanja črk: program "x" sekund ponavlja: izpiše črko, uporabnika vpraša, da jo čim prej ponovi (in pritisne Enter) in preveri pravilnost
# ko čas poteče, izpiše odstotek rpavilnih odgovorov

dolzinaTrajanja = 10
pravilniVnos = 0
vsiVnosi = 0
crke = list("abcdefghijklmnoprstuvz")
t1 = time.time()

while True:
  t2 = time.time()
  if t2 - t1 > dolzinaTrajanja: 
    break
  else:
    randomCrka = random.choice(crke)
    print(randomCrka)
    vnos = input("čimprej vnesi izpisano črko: ")
    if vnos == randomCrka:
      pravilniVnos += 1
      vsiVnosi += 1
      continue
    else: 
      vsiVnosi += 1

odstotek = (pravilniVnos/vsiVnosi) * 100
print(f"pravilnih vnosov je bilo {odstotek} %")

