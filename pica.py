# vpraša za dodatke na pici, jih shranjuje, na koncu izpiše
dodatki = ""

while True: 
  print("izbrani dodatki: ", dodatki)
  vnos = input("vnesi željene dodatke: ")
  if vnos == "":
    break
  dodatki = dodatki + ", " + vnos

print("izbrani dodatki na pici: ", dodatki)


# boljša verzija programa
dodatki = ""

while True:
  print("izbrani dodatki: ", end="") # najprej izpišemo dodatke
  if dodatki == "":
    print("nič")
  else:
    print(dodatki)
  
  vnos = input("kaj dodamo na pico? ")
  if vnos == "":
    break
  
  if dodatki != "":
    dodatki = dodatki + ", " 

  dodatki += vnos

print("izbrani dodatki na pici: ", dodatki)
