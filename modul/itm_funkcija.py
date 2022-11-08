def itm(masa, visina):
  
  if visina == 0: # namerno sesutje programa
    raise Exception("kritična napaka, višina ne sme biti 0")
  
  if visina > 3:
    visina = visina/100
  
  try: 
    itm = masa/visina**2
  except ZeroDivisionError:
    print("ITM ne morem izračunati")
    itm = "N/A"
  return itm


def presodi_itm(itm):
  if itm < 18.5:
    return "nedohranjenost"
  elif itm <25:
    return "normalna telesna teža"
  elif  itm < 30:
    return "povišana telesna teža"
  elif itm < 35:
    return "debelost 1. razreda"
  elif itm < 40:
    return "debelost 2. razreda"
  elif itm > 40:
    return "debelost 3. razreda"
  
