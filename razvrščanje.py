# razvrščanje odgovorov glede na vpisano starost
starost = int(input("vpišite starost: "))

if (starost < 18):
  print("premladi ste")
elif (18 <= starost <= 25):
  print("ravno prav ste stari")
elif (25 <= starost <= 35):
  print("starate se")
else:
  print("prestari ste")
