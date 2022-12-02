import random

seznam_imen = []

while True:
  ime = input("vnesi ime študenta: ")
  if ime == "":
    break
  seznam_imen.append(ime) 

while True:
  nakljucno_ime = random.randint(0, len(seznam_imen)-1)
  # nakljucno_ime = random.choice(seznam_imen)
  
  vnos = input("ENTER za naključni izbor, q za izhod: ")
  if vnos == "":
    print(f"na vprašanje naj odgovori: {seznam_imen[nakljucno_ime]}")
    # print(f"na vprašanje naj odgovori: {nakljucno_ime}")
  elif vnos.upper() == "Q":
    print("adijo")
    quit()
