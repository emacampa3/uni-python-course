# funkcija, ki kot vhodni argument sprejme ime datoteke, prebere števila v datoteki in jih kot integers shrani v seznam, ki ga funkcija tudi vrne
def branje(datoteka):
  with open(datoteka, "r") as fv: # odpremo datoteko za branje
    vsebina = fv.read() # vsebina je seznam nizov znotraj datoteke
    seznam = vsebina.split() # razbijemo vsebino pri presledkih
    seznamStevil = [] # prazen seznam
    for i in seznam: # iteriramo čez seznam
      seznamStevil.append(int(i)) # dodajamo na prazen seznam ter hkrati spreminjamo v integers
  return seznamStevil

stevila = branje("stevila1.txt") # ker je open-close svoja mapa, moraš cd do te mape, da se pravilno izpiše na terminalu 
print(stevila) # terminal vrne: [1, 4, 6, 7, 4, 12, 7, 0, 3, 2, 45, 8, 0, 5, 34, 8, 9, 12, 44, 7, 8, 99, 33, 7, 88]

# funkcija izračuna in vrne povprečno vrednost za seznamStevil
def povprecje(seznam):
  return sum(seznam)/len(seznam)

povprecje = povprecje(stevila) # vnesemo nek že definiran seznam
print(povprecje) # izpis na terminalu 18.12


# izpiše števila iz seznama v novo datoteko tako, da sta v vsaki vrstici zapisani 2 števili
# znak se spreminja glede na to, v kateri vrstici smo
def pisi(seznamStevil, datoteka, vVrstici = 2):
  with open(datoteka, "w") as fi:
    vrstice = 0
    for i in seznamStevil: # gre čez vsa števila v datoteki
      vrstice += 1
      if vrstice % vVrstici == 0: # če je vrstica deljiva z 2, gre naslednje število v novo vrstico, sicer je vmes tabulator
        znak = "\n"
      else:
        znak = "\t"
      fi.write(f"{i}{znak}") 
        
seznamStevil = branje("stevila1.txt") # datoteka, iz katere beremo števila
pisi(seznamStevil, "stevilaIzhodnaDatoteka.txt") # ustvari nov file z števili, kjer sta vedno le dve števili na vrstico


# funkcija, ki izračuna min in max v seznamu
def minMax(seznam):
  return (min(seznam), max(seznam))

# calling the function
minmax = minMax(stevila)
print(minmax) # na terminalu se izpiše n-terka: (0,99)

# funkcija, ki lepše zapiše min in max seznama
def zapis(minMax): # ustvarimo novo datoteko, kamor zapišemo rezultat
  with open("rezultat.txt", "w") as f:
    # ker je n-terka, dostopamo do števil s pomočjo indeksov
    f.write(f"""največje število: {minMax[1]} najmanjše število: {minMax[0]}""")

# calling the function: ustvari novo mapo, kjer je zgornje besedilo
mm = zapis(minmax)

