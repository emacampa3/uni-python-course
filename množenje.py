import random

# računalnik generira dve števili, ju sešteje in vpraša za rešitev vsote
x = random.randint(1, 100)
y = random.randint(1, 100)

z = x + y

ugibanje = int(input(f"vsota {x} in {y}: "))

if ugibanje == z:
  print(f"pravilno")
else:
  print(f"napačno, rešitev: {x} + {y} = {z}")



# generira 2 random celi števili
a = random.randint(1, 10) 
b = random.randint(1, 10)

# a in b spremenimo v string, saj bi z int nastal error
racun = str(a) + " * " + str(b) + " = " # vprašamo za rešitev
c = input(racun)

if c == "": # empty string
  print(f"nasvidenje")
else:
  c = int(c) # spremenimo v integer, da lahko primerjamo
  if c == a*b:
    print(f"pravilno")
  else:
    print(f"napačno")
    print(racun, a*b, sep="")
