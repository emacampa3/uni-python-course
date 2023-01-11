# Napišite program, ki bo omogočil vnos podatkov za poljubno število izdelkov. Za vsak izdelek je potrebno vnesti kodo izdelka, ime izdelka in ceno. Podatki se naj shranjujejo v slovar, kjer naj bo koda izdelka ključ, vrednost pa seznam, kjer je prva vrednost ime izdelka, druga pa cena. Cena mora biti vnesena kot realno število. Program naj spraˇsuje po podatkih, dokler namesto kode izdelka uporabnik ne pritisne samo ”Enter”. Ce se za ceno vnese nekaj, kar ni število, naj program ponovno vpraˇsa po ceni.

izdelki = {}
while True:
  kodaIzdelka = input("vnesite kodo izdelka ali 'Enter': ")
  if kodaIzdelka == "":
    break
  imeIzdelka = input("vnesite ime izdelka: ")
  while True:
    try:
      cenaIzdelka = float(input("vnesite ceno izdelka: "))
      break
    except:
      print("cena mora biti število")
      continue
  izdelki[kodaIzdelka] = [imeIzdelka, cenaIzdelka] # shranimo v slovar

print(izdelki)
