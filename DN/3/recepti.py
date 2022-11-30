import random

seznam = [{'Recept': "KROMPIR Z JAJCI\nSkuhaj krompir trdo kuhana jajca, oboje po kuhanju olupi, krompir pa še popeči v ponvi. Bon Appétit!\n",'Glavne': [0], 'Pomozne': [2]}, {'Recept': "KROMPIR S KLOBASO\nSkuhaj krompir, ga olupi in popeči v ponvi. Za tem popeči še klobaso. Bon Appétit!\n",'Glavne': [0], 'Pomozne': [5]}, {'Recept': "MAKARONI S PARADIŽNIKOVO OMAKO\nSkuhaj makarone, pogrej paradižnikovo omako, zmešaj in pojej. Bon Appétit!\n",'Glavne': [1], 'Pomozne': [0]}, {'Recept': "MAKARONI S TUNINO OMAKO\nSkuhaj makarone, ločeno popraži tuno, zmešaj z makaroni in pojej. Bon Appétit!\n",'Glavne': [1], 'Pomozne': [1]}, {'Recept': "RIŽOTA S PIŠČANCEM\nSegrej ponev, popeči piščanca, dodaj začimbe in riž. Kuhaj 15min in pojej. Bon Appétit!\n",'Glavne': [2], 'Pomozne': [3]}, {'Recept': "RIŽOTA Z JAJCI\nSkuhaj riž, ločeno v ponvi speči jajca in jih dodaj k rižu. Bon Appétit!\n",'Glavne': [2], 'Pomozne': [2]}, {'Recept': "SOLATA Z JAJCI\nSkuhaj trdo kuhana jajca, umij in nareži solato. Nareži še jajca, in jih zmešaj s solato. Bon Appétit!\n",'Glavne': [3], 'Pomozne': [2]}, {'Recept': "SOLATA Z PARADIŽNIKOM\nOperi solato in paradižnik, oboje nareži in zmešaj. Bon Appétit!\n", 'Glavne': [3], 'Pomozne': [4]}]

glavne_sestavine= ["krompir", "makaroni", "riž", "solata", ]
dodatne_sestavine= ["paradižnikova omaka", "tuna", "jajca", "piščanec", "paradižnik", "klobasa"]

while True:
  nakljucni_recept = random.randint(0, len([i for i in seznam if i])-1)
  
  print(f"""
  izberaš lahko med dvema načinoma delovanja programa:

  Izberi:
  - N za naključno izbran recept
  - S za izbiro recepta glede na sestavine
  """)

  izbira = input("vpiši eno izmed črk: ")

  if izbira.upper() == "N":
    print(f"naključno izbran recept: {seznam[nakljucni_recept]['Recept']}")
    break

  elif izbira.upper() == "S":
    for gl_sestavina in glavne_sestavine:
      print(gl_sestavina)
      gl_sestavina_input = input(f"ali imaš doma: {gl_sestavina}? DA/NE: ")
      if gl_sestavina_input.upper() == "DA":

        index_gl_sestavine = glavne_sestavine.index(gl_sestavina) # index glavne sestavine v seznamu glavne_sestavine
        for sestavina in seznam:
          mesto_gl_sestavine_in_list = ''.join(map(str, sestavina['Glavne']))

          if index_gl_sestavine == int(mesto_gl_sestavine_in_list): # če se index glavne sestavine v seznamu Glavne_sestavine ujema z indeksom v seznamu
            index_pomozne_sestavine_in_list = ''.join(map(str, sestavina['Pomozne']))
            index_dodatna_sestavina = int(index_pomozne_sestavine_in_list)
            po_sestavina_input = input(f"ali imaš doma: {dodatne_sestavine[index_dodatna_sestavina]}? DA/NE: ")

            if po_sestavina_input.upper() == "DA":
              print(f"predlagam: {sestavina['Recept']}")
              quit()
            else: 
              continue
        break
      elif gl_sestavina_input.upper() == "NE":
        continue
      else: 
        print("neveljaven vnos")
        continue
    print("\nžal ni nobenega ustreznega recepta\n")
    quit()
