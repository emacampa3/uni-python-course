import random


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


class Koza(Zival):
  def __init__(self, ime, spol, starost):
    Zival.__init__(self, "Koza", ime, spol, starost)

  # definirano samo za podrazred
  def dajeMleko(self, starost):
    # returns True èe sta oba pogoja izpolnjena, sicer je False
    return self.spol == "Z" and self-starost > 12

  def mladicek(self, kozel):
    ok = True
    if not isinstance(kozel, Koza):  # èe kozel ni objekta Koza
      ok = False
    if self.spol != "Z":
      ok = False
    if self.starost <= 12:
      ok = False
    if kozel.spol != "M":
      ok = False
    if kozel.starost <= 12:
      ok = False

    if ok:
      spol = random.sample(["M", "Z"], 1)[0]  # izberemo 1 string v objektu
      if spol == "M":
        ime = "Jaka"
      else:
        ime = "Pika"
      return Koza(ime, spol, 0)

    else:
      print("mladicka ni mogoèe narediti")
      return None


kJana = Koza("Jana", "Z", 10)
# na novem objektu, ki je podrazred Zivali, izvedemo metodo nadrazreda
kJana.postaraj(10)
print(kJana)

kJanez = Koza("Janez", "M", 23)
kMladicek1 = kJana.mladicek(kJanez)
print(kMladicek1)
