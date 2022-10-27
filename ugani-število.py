import random

nakljucnoŠtevilo = random.randint(0, 10)
x = 0 # števec
while True:
  ugibanje = int(input("ugibaj število: "))
  x += 1
  if ugibanje < nakljucnoŠtevilo:
    print("Ne, premalo si rekel")
  elif ugibanje > nakljucnoŠtevilo:
    print("Ne, prevec si rekel")
  else:
    break

print(f"bravo, uganil si v {x} poskusih")


# bolj napredna verzija 
nakljucno = random.randint(0, 1000)
x = 0 # števec

while True:
  ugibanje = int(input("ugibaj število: "))
  x += 1
  if ugibanje < nakljucno:
    print(f"vneseno število je premajhno")

  elif ugibanje > nakljucno:
    print(f"vneseno število je preveliko")
  else:
    break

  if abs(ugibanje-nakljucno) > 500:
    print("ledeno")
  elif abs(ugibanje-nakljucno) > 200:
    print("mrzlo")
  elif abs(ugibanje-nakljucno) > 100:
    print("toplo")
  elif abs(ugibanje-nakljucno) > 50:
    print("vroce")
  else:
    print("zelo vroce")
    
print("bravo, ugnu si v", x,"poskusih")
