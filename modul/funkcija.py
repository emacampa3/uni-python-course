# MODUL ZA handling-erros.py: ponavljajočo se funkcijo daš v svojo datoteko, izrežeš iz originalne datotete
# na vrhu handling-errors.py: import input_float from modul.py oz. import input_int from modul.py

def input_float(besedilo):
  while True:
    stevilka = input(besedilo)

    try:
      stevilka = float(stevilka)
    except:
      print("prosim, vnesi številko")
    else:
      return stevilka
