# Napišite funkcijo, ki bo vrnila imena vseh datotek v trenutni mapi z izbrano konˇcnico ter njihovo dolžino. Izbrana končnica naj bo argument funkcije. Funkcija naj rezultat sicer vrne kot seznam n-terk, kjer naj bo prva vrednost n-terke ime datoteke, druga pa njena dolžina v znakih. Ce v mapi ni datotek z izbrano končnico, naj funkcija vrne prazen seznam. Namig: Seznam vseh datotek v poljubni mapi vrne funkcija listdir, ki se nahaja v modulu os. Trenutno mapo lahko izberete tudi tako, da za ime mape vnesete "." (vključno z narekovaji). Funkcijo tudi uporabite in rezultat shranite v neko spremenljivko!

import os

def funkcija(koncnica): # argument je izbrana končnica
  seznamdatotek = os.listdir() 
  # zanimajo nas le datoteke z določeno končnico
  seznamUstreznih = []
  nKončnica = len(koncnica) + 1 # koliko je končnica dolga (končnica je brez pike)
  for i in seznamdatotek:
    if i[-nKončnica:] == ("." + koncnica): # pogledamo zadnje znake (če je nKončnica enako 4, pogledamo zadnje 4 znake) od -4 do konca
      with open(i, "r") as f: # število znakov v datoteki: preberemo datoteko, pogledamo dolžino
        nZnakov = len(f.read()) # read prebere celo datoteko, z len pa dobimo dolžino
      seznamUstreznih.append((i, nZnakov)) # v seznam dodamo n-terko (ustvarimo z okroglima oklepajema)
  
  return seznamUstreznih

# uporaba funkcije
datoteke = funkcija("py")
print(datoteke)

