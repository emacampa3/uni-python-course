# program ponavlja v neskončnost do preklica "izhod"
vnos = input("vnesi kar želiš: ") # ni primer dobre prakse (podvojena koda)
while vnos != "izhod":
  print(vnos)
  vnos = input("vnesi kar želiš: ")

# boljša praksa
vnos = "" # prvič ko gre čez, vnos != izhodu, zato gre čez zanko, do inputa in prvič vpraša za vnos
while vnos != "izhod": # zanka se neha izvajati, ko se evalvacija spremeni v False
  if vnos != "izhod": # če vnos ni enak besedi "izhod", print vnos
    print(vnos)
  vnos = input("vnesi kar želiš: ")

# while True se ponavlja v neskončnost, while False se ne izvaja (ponovi se 0x)

# najbolj optimizirana verzija programa
while True:
  vnos = input("vnesi kar želiš: ")
  if vnos == "izhod": # če je to True, prekine zanko, sicer nadaljuje in izvede print
    break # gre iz zanke in nadaljuje pod zanko: konec programa
  elif vnos == "prekleto" or vnos == "tristo kosmatih medvedov":
    print("grdih besed ne podpiram") 
    continue # prekine izvajanje zanke: nadaljuje naslednji cikel zanke: zopet vpraša za input
  print(vnos)

