# Prejšnjo funkcijo popravite tako, da bo rezultat datoteka, kjer so stolpci loceni s tabulatorji(ˇ \t). 
# Stolpci naj bodo: ime, tip (def na začetku), razred (prazno ob funkciji, sicer class), argumenti (ločeni z vejico)

import os

def kopirajDef(imeDatoteke):
  if imeDatoteke[-3:] != ".py": 
    raise Exception("vhodna datoteka ni .py file")
  if not os.path.exists(imeDatoteke): 
    raise Exception("vhodna datoteka ne obstaja")

  imeDatotekeIzhodna = imeDatoteke[:-3]+".txt" 

  # odpremo obe datoteki
  with open(imeDatoteke, "r") as fr:
    with open(imeDatotekeIzhodna, "w") as fw:
      fw.write("Ime \t Tip \t Arg \t Razred")

      for line in fr:
        line2 = line.lstrip()
        # razred oz. class
        if line.startswith("class "):
          razred = line[6:].lstrip() # brez prvih 6 znakov in whitespace na levi
          razred = razred.split("(", maxsplit=1)[0]
          razred = razred.split(":", maxsplit=1)[0].rstrip() # odstranimo whitespace na desni

        if line2.startswith("def "):
          # ime funkcije
          defFun = line2[4:] # iz te vrste odstranimo prve 4 znake (odstranimo def in presledek)
          defFun = defFun.split("(", maxsplit=1) # ločimo pri ločilu oklepaj: maxsplit pomeni da bo vse ostalo zajel kot en argument
          ime = defFun[0]  # izberemo samo prvi element: to je ime funkcije
          
          # argumenti
          arg = defFun[1] 
          arg = arg.split("):")[0]

          # tip
          if line.startswith("def "):
            tip = "funkcija"
            razred = ""
          else:
            tip = "metoda"

          # zapišemo v novo datoteko .txt
          fw.write(f"{ime} \t {tip} \t {arg} \t {razred}")

kopirajDef("python/open-close/copy-funkcija.py") # caaling the function
