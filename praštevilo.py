# je vneseno število praštevilo?
stevilo = int(input("vnesi število med 1 in 20: "))
preizkus = 2
for i in range(preizkus, stevilo):
  if (stevilo % preizkus) == 0: # če je ostanek pri deljenju = 0, potem je število deljivo z 2, torej ni praštevilo
    print(f"število {stevilo} ni praštevilo")
    break
  else:
    print(f"število {stevilo} je praštevilo")
    break
