# Napišite funkcijo, ki vam vrne seznam vseh Pythonovih datotek v izbrani mapi. Privzeta vrednost naj bo trenutna mapa. Namig: Trenutno mapo določimo tako, da v nizu namesto poti ozirom imena mape navedemo le piko(".")
def seznamPythonDatotek(mapa):
  from os import listdir
  seznamVseh = listdir(mapa)
  seznamPyhton = [] # nov seznam, kamor kopiramo vse datoteke s končnico .py
  for i in seznamVseh: # gremo čez cel seznam
    if i[-3:] == ".py": # če se zadnje tri črke ujemajo, dodaj na nov seznam
      seznamPyhton.append(i)

  return seznamPyhton


# Napiši funkcijo mojInput, ki bo delovala tako, kot dela v Pythonu 3 funkcija input tako v verzijo Pythona 3 kot tudi v verziji 2. Enakovredna funkcija v Pythonu 2 je raw_input.
def mojInput(tekst):
  from sys import sys, raw_input
  if sys.version_info.major == 3: # tu pridobimo verzijo nameščenega pythona
    return input(tekst)
  else:
    return raw_input(tekst)


# Napišite funkcijo, ki sprejme kot vhodni argument mapo (privzeto naj bo trenutna mapa). Nato naj vse datoteke iz te mape premakne v podmape, katerih ime je enako prvem znaku imena datoteke. Velikost črke (mala/velika) ignorirajte. Če mapa s takim imenom še ne obstaja, naj jo ustvari.
def funkcija(mapa):
  import os
  seznamVseh = os.listdir(mapa) # pridobimo vse datoteke
  for i in seznamVseh: # gremo čez vse datoteke tega seznama
    prviZnak = i[0].upper() # prvi znak spremenimo v veliko črko
    novaMapa = mapa+"/"+prviZnak
    try: # če mapa s tem imenom še ne obstaja, jo ustvarimo z os.mkdir
      if not os.path.exists(prviZnak):
        os.mkdir(novaMapa)
      os.rename(mapa+"/"+i, novaMapa+"/"+i) # preimenujemo datoteko s funkcijo os.rename: Kot začetno ime določimo niz, kjer združimo izbrano mapo (niz, ki ga funkcija sprejme kot argument), "/" (poševnico, ki se uporablja kot ločilo pri poti do datoteke med mapami) in ime datoteke (ki jo obdelujemo v tej ponovitvi for zanke, kot končno ime pa enako, le da namesto izbrane mape dodamo niz, kot smo ga oz. bi ga (če je mapa že obstajala) uporabili pri oblikovanju niza za kreiranje mape v točki b
    except:
      print(f"datoteke {i} ne morem premakniti v mapo {novaMapa}")


# Napiši funkcijo, ki bo vrnila niz, ki prestavlja trenutni datum in čas v slovenskem formatu, torej recimo "31.12.2019 13:45"
def trenutniČas():
  import datetime
  now = datetime.datetime.now() # pridobimo trenutni čas
  return now.strftime("%d.%m.%Y %H:%M")

čas = trenutniČas()
print(čas)


# Napišite funkcijo, ki bo izračunala, koliko dni je od trenutnega datuma do določenega datuma. Vrne naj število dni, s tem da naj negativno število pomeni, da je določen datum v preteklosti. Funkcija naj določen datum sprejme kot argument v obliki niza v formatu "DD. MM. LLLL"
def kolikoDni(datum):
  import datetime
  now = datetime.datetime.now() # pridobimo trenutni čas (datum in ura)
  now = now.date() # dobimo samo datum, brez ure
  # now = datetime.date.now() alternativa predhodnih 2 vrstic
  datum = datetime.datetime.strptime(datum, "%d.%m.%Y") # preberemo vnešen datum, in ga spremenimo v čas v določenem formatu
  datum = datum.date()
  razlika = datum - now

  # print(razlika.days)
  return razlika.days

dnevi = kolikoDni("11.04.2000")
print(dnevi)
# alternativa s print(): samo pokličeš funkcijo kolikoDni() in notri kot string vneseš datum, brez printa za tem


# Napišite igro za urjenje spomina. Igra naj vam izpiše 10 slučajno izbranih črk, ki naj bodo na zaslonu izpisane 5 sekund. Nato naj zaslon navidezno izbriše in uporabniku omogoča vnos teh črk(lahko kot en niz). Nato naj izračuna, koliko črk je uporabnik vpisal in prešteje, koliko je pravilnik. Vrstni red črk ni pomemben. Če uporabnik vnese več kot 10 znakov, naj upošteva samo prvih 10. Po vsaki igri naj izpiše število pravilno navedenih črk in vpraša uporabnika, ali želi ponovno igrati igro. Prav tako naj število pravilno navedenih črk shranjuje. Ko uporabnik ne želi več ponovni igrati igre, naj izpiše število poizkusov, povprečno(na 2 decimalni mesti natančno), največje in najmanjše število pravilno navedenih črk
import random, time
crke = "abcčdefghijklmnoprsštuvzž"
seznamUgibanj = []

while True:
  izbor = random.sample(crke, 10) # naključno izbere 10 črk iz niza, dobimo seznam, kjer je vsak element ena črka
  izborNiz = "".join(izbor) # metodo .join uporabimo na praznem nizu (ker nismo ustvarili novega), argument pa je seznam izbor
  print("zapomnite si sledeče črke:")
  print(izborNiz)
  time.sleep(4)
  print("\n"*10)
  vpisanNiz = input("""vnesi črke, ki so bile prikazane
  črke: """)
  pravilnoUgibanje = 0
  for i in vpisanNiz[:10]:
    if i in izborNiz:
      pravilnoUgibanje += 1
  print(f"pravilno ste vnesli {pravilnoUgibanje} od 10-ih črk")
  seznamUgibanj.append(pravilnoUgibanje)
  nadaljevanje = input("vnesi prazen niz za novo igro oz. karkoli drugega za konec igre")
  if nadaljevanje != "":
    break

if len(seznamUgibanj) > 0:
  print(f"""
  število poskusov: {len(seznamUgibanj)}
  povprečno število pravilno navedenih črk: {sum(seznamUgibanj)/len(seznamUgibanj):.2f}
  najmanjše število pravilno navedenih črk: {min(seznamUgibanj)}
  največje število pravilno navedenih črk: {max(seznamUgibanj)}""")


# Napišite program, ki bo izpisal 5 slučajno izbranih imen, ločenih z vejico. Da boste lahko to storili, morate prej ustvariti seznam z vsaj 20 imeni. Nato mora uporabnik v pravilnem vrstnem redu izpisati vsa imena, ločena z vejico, točno tako, kot so zapisana zgoraj. Program naj preveri, ali je uporabnik pravilno izpisal vsa imena in če, koliko časa je uporabnik potreboval za izpis. Uporabnik naj ima tri možnosti za vnos imen. Šteje se najboljši čas, ko je uporabnik pravilno prepisal vsa imena. Leta naj se nato izpiše ter uporabnika vpraša, ali želi "ponoviti vajo" z novimi imeni.
import random, time
imena = ['Franc', 'Janez', 'Marko', 'Ivan', 'Anton', 'Andrej', 'Jožef', 'Jože', 'Luka', 'Peter', 'Marjan', 'Matej', 'Tomaž', 'Milan', 'Aleš', 'Branko', 'Bojan', 'Domen', 'Vid', 'Danijel', 'Goran', 'Mark', 'Tim', 'Stanko', 'Mihael', 'Leon', 'Matevž', 'Urban', 'Sašo', 'Anja', 'Katja', 'Sara', 'Sonja', 'Tatjana', 'Jožefa', 'Katarina', 'Tanja', 'Tina', 'Milena', 'Alenka', 'Vesna', 'Nika', 'Martina', 'Majda', 'Urška', 'Ivana', 'Špela', 'Tjaša', 'Frančiška', 'Anica', 'Helena', 'Dragica', 'Darja', 'Nada', 'Terezija', 'Kristina', 'Simona', 'Lara', 'Danica', 'Marjeta', 'Olga', 'Suzana', 'Zdenka', 'Neža', 'Lidija', 'Ema', 'Sabina', 'Janja', 'Marta', 'Antonija', 'Vida', 'Angela', 'Ivanka', 'Maša', 'Silva', 'Zala', 'Veronika', 'Karmen', 'Darinka', 'Aleksandra', 'Lana', 'Anita', 'Ljudmila', 'Klara', 'Kaja', 'Brigita', 'Alojzija', 'Jana','Lucija', 'Metka', 'Monika', 'Lea', 'Stanislava', 'Natalija', 'Cvetka', 'Nevenka', 'Jasmina', 'Štefanija', 'Elizabeta', 'Renata', 'Marjana', 'Branka', 'Tamara', 'Julija', 'Slavica', 'Saša', 'Hana', 'Manca', 'Klavdija', 'Ajda', 'Bojana', 'Bernarda', 'Erika', 'Teja', 'Vera', 'Danijela']

while True:
  vsiCasi = []
  izborImen = random.sample(imena, 5) # izbere 5 imen
  nizIzbora = ", ".join(izborImen)
  for i in range(3):
    print("vnesite sledeči niz:")
    print(nizIzbora)
    t1 = time.time()
    vnešeniNiz = input("vaš vnos: \n")
    cas = time.time() - t1 # izračunamo uporabnikov čas tipkanja
    if vnešeniNiz == nizIzbora:
      print(f"bravo, brez napak! za vpis ste potrebovali {cas:.3f} sekund")
      vsiCasi.append(cas)
    else: 
      print("zatipkali ste se")
  if len(vsiCasi) == 0:
    print("nikoli niste pravilno vtipkali imen")
  else:
    print(f"pravilno ste pretikali {len(vsiCasi)}-krat. \nVaš najboljši čas je {min(vsiCasi): .3f} sekund")
  
  konec = input("Pritisnite 'n' za novo igro ali karkoli drugega za konec: ")
  if konec != "n":
    break
