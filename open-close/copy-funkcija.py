import os

# Napišite funkcijo, ki iz prek vhodnega parametra dobi pythonovo datoteko in prekopira iz te datoteke v novo datoteko(ki naj ima isto ime kot prva, le koncnico "txt") vse vrstice, ki se zacnejo z def
def kopirajDef(imeDatoteke):
  if imeDatoteke[-3:] != ".py": # preverimo zadnje 3 znake, če je file pythonova datoteka
    raise Exception("vhodna datoteka ni .py file")
  if not os.path.exists(imeDatoteke): # preverimo da datoteka obstaja
    raise Exception("vhodna datoteka ne obstaja")
    
  imeDatotekeIzhodna = imeDatoteke[:-3]+".txt" # vse razen zadnjih treh znakov

  # odpremo obe datoteki
  with open(imeDatoteke, "r") as fr:
    with open(imeDatotekeIzhodna, "w") as fw:
      for line in fr:
        # if line[:4] == "def ": če se prvi štirje znaki ujemajo
        if line.startswith("def "):
          fw.write(line) # če se ujemajo znaki, jo prepišemo v novo datoteko

kopirajDef("copy-funkcija.py") # kličemo funkcijo
