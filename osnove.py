import random # za celo stran

# curly and square brackets on Windows: ALt Gr + FG/BN
# int(5,99) je še vedno 5, ne zaokrožuje se navzgor
# 22/3 = 7.33333 float 22//3 = 7 celi del deljenja, 22%3 nam da le ostanek pri deljenju (1): koristno pri ugotavljanju deljivosti dveh števil, sodosti/lihosti
# potenca: 2**3 = 8

# print(sep="") prazen niz
# print(sep=", ") ločeno z vejico in presledkom
# print(end="") privzeto ločilo je znak za novo vrstico, lahko ga nadomestimo


ime = input("vnesi svoje ime: ")
print("pozdravljena,", ime) 
print(f"pozdravljena, {ime}")


# seštevanje števil
a = int(input("Vnesi število: "))
b = int(input("Vnesi drugo število: "))
print(a+b)


# dolžina outputa je odvisna od vpisane ocene
ocena = int(input("Koliko si pisal statistiko? "))
print("H" + "u"*ocena + "do")


# output je odvisen od inputa
ocena = float(input("Koliko si pisal statistiko? "))
if ocena < 50:
  print("Manj kot 50%, bedno")
else:
  faktor = int(ocena/10-4)
  print("Faktor je: ", faktor)
  print("H" + "u"*faktor + "do")


# output je odvisen od inputa
ime = input("Ime študenta: ")
predmet = input("Ime predmeta: ")
ocena = input("Ocena: ")
print(f"{ime} je pri predmetu {predmet} dobil/a oceno {ocena}")
# print(ime, " je pri predmetu ", predmet, " dobil/a oceno", ocena, ".", sep="") drugačen zapis


# število U je odvisno od inputa
stevilo = int(input("Kako super se počutiš? Odgovori s števili med 1 in 10: "))
print("S" + stevilo*"u" + "per!")


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


# output odvisen od inputa
ime = input("kako ti je ime? ")
if ime == "Ema":
  print(f"moje sožalje, {ime}")
else:
  print(f"čudovito ime!")


# seštevanje cen in izračun povprečne cene
kruh = 0
kruh += int(input("vnesi ceno kruha: "))
kruh += int(input("vnesi ceno kruha: "))
kruh += int(input("vnesi ceno kruha: "))
print(f"povprečna cena kruha je {kruh/3}")



