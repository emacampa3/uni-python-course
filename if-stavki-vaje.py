# deljenje z ostankom
stevilo1 = int(input("vnesi celo število: "))
stevilo2 = int(input("vnesi celo število: "))

if stevilo2 < stevilo1: 
  # rezultat = round((stevilo1 / stevilo2), 2)
  rezultat = stevilo1 // stevilo2 # deljenje celih števil
  ostanek = stevilo1 % stevilo2
  if ostanek == 0:
    print(f"{stevilo1} deljeno z {stevilo2} je {rezultat}")
  else:
    print(f"{stevilo1} deljeno z {stevilo2} je {rezultat}, ostanek je {ostanek}")
else: 
  print("drugo število mora biti manjše od prvega")


# izpis ocene 
stevilo = float(input("vnesi število med 0 in 100: "))
if stevilo < 0 or stevilo > 100:
  print("število mora biti med 0 in 100")
elif stevilo < 50:
  print("negativna ocena na izpitu")
elif stevilo < 60:
  print("ocena izpita = 6")
elif stevilo < 70:
  print("ocena izpita = 7")
elif stevilo < 80:
  print("ocena izpita = 8")
elif stevilo < 90:
  print("ocena izpita = 9")
elif stevilo < 100:
  print("ocena izpita = 10")


# izpiše vneseno število znakov
stevilo = int(input("število med 0 in 60: "))
if stevilo < 0 or stevilo > 60:
  print("izpis ni mogoč")
else: 
  print(stevilo * "#")


# response je odvisen od deljivosti vnesenega števila
stevilo = int(input("vnesi celo število: "))
if stevilo % 2 == 0 and stevilo % 3 != 0:
  print(f"število {stevilo} je deljivo z 2, s 3 pa ne")
elif stevilo % 3 == 0 and stevilo % 2 != 0:
  print(f"število {stevilo} je deljivo z 3, z 2 pa ne")
elif stevilo % 2 == 0 and stevilo % 3 == 0:
  print(f"število {stevilo} je deljivo z 2 in 3")
else:
  print(f"število {stevilo} ni deljivo ne z 2, ne s 3")

# boljša rešitev
if stevilo % 2 == 0:
  if stevilo % 3 == 0:
    print(f"število {stevilo} je deljivo z 2 in 3")
  else: 
    print(f"število {stevilo} je deljivo z 2, s 3 pa ne")
else: 
  if stevilo % 3 == 0:
    print(f"število {stevilo} je deljivo z 3, z 2 pa ne")
  else:
    print(f"število {stevilo} ni deljivo ne z 2, ne s 3")


print((1**2+2**2+3**2)/(3+4)) # 2
print(7%3) # ostanek je 1
print((2+2**1+2**2+2**3)**(1/4)) # 2


# izračun hipotenuze
kateta1 = float(input("vnesi dolžino prve katete: "))
kateta2 = float(input("vnesi dolžino druge katete: "))

hipotenuza = round((kateta1**2 + kateta2*+2)**(1/2), 2)

print(f"prva kateta, dolžine {kateta1}, in druga kateta, dolžine {kateta2}, pogojujeta hipotenuzo dolžine {hipotenuza}")
