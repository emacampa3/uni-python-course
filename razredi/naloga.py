import datetime

class Pacient():
  def __init__(self, ime, priimek, r_dan, r_mesec, r_leto):
    self.ime = ime
    self.priimek = priimek
    self.rdan = r_dan
    self.rmesec = r_mesec
    self.rleto = r_leto
  
  def starost(self):
    # starost = danes - rojen (razlika je v dnevih: za razliko v letih moramo deliti s 365)
    danes = datetime.datetime.today()
    # rojstvo pretvorimo iz besedila v datum
    rojstvo = datetime.datetime.strptime(str(self.rdan) + "." + str(self.rmesec) + "." + str(self.rleto), "%d.%m.%Y")
    razlika = danes - rojstvo
    print(f"star si: {int(razlika.days/365.25)}")
  
Janez = Pacient("Janez", "Novak", 1, 3, 1995) # števila so integers
Janez.starost()

