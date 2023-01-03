class Zival:
  def __init__(self, vrsta, ime, spol, starost):
    self.vrsta = vrsta
    self.ime = ime
    if spol not in ("M", "Z"):  # mora biti ena izmed možnosti v n-terki
      raise Exception("spol mora biti M ali Z")
    self.spol = spol  # sicer kreiramo objekt
    if not isinstance(starost, (int, float)):  # èe starost ni številskega tipa
      raise Exception("starost mora biti število")
    self.starost = starost  # sicer kreiramo objekt

  def __str__(self):  # lahko sprejme samo self
    return f"{self.vrsta}: {self.ime}, {self.spol}, {self.starost}"

  def preimenuj(self, novoIme):  # nova nerezervirana metoda
    self.ime = novoIme

  def postaraj(self, mesec=1):
    self.starost += mesec


kPika = Zival("koza", "Pika", "Z", 13)
print(kPika)

# poklièemo novo metodo, ki preimenuje žival
kPika.preimenuj("Pikica")
print(kPika)

# klièemo novo metodo
kPika.postaraj(14)
kPika.postaraj()
print(kPika)
