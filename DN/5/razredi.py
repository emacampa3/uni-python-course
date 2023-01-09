class Clovek():
  def __init__(self, ime, starost, stevilo_las):
    self.ime = ime
    self.starost = starost
    self.stevilo_las = stevilo_las

  def __str__(self):  # lahko sprejme samo self
    return f"{self.ime}: starost = {self.starost}, število las = {self.stevilo_las}"
  
  def plesast(self):
    if self.stevilo_las < 70000:
      print(f"{self.ime}, žal obstaja verjetnost, da si plešast!")
    elif self.stevilo_las >= 70000:
      print(f"{self.ime}, človeški Wookiee si!")
  
  def smrt(self):
    if self.starost > 50:
      print("Morda boš kmalu šel po gobe!")
    else:
      print(f"Uživaj življenje, dokler ga še lahko, {self.ime}!")

class Azijec(Clovek):
  def __init__(self, ime, starost, povprecna_ocena):
    Clovek.__init__(self, ime, starost, povprecna_ocena)
    self.povprecna_ocena = povprecna_ocena
  
  def __str__(self):  # lahko sprejme samo self
    return f"{self.ime}: starost = {self.starost}, povprečna ocena = {self.povprecna_ocena}"

  def klofuta(self):
    if self.starost < 35:
      if self.povprecna_ocena < 9:
        print(f"{self.ime}, doma te čaka klofuta!")
      else:
        print(f"Še zmeraj ni dovolj dobro, {self.ime}!")
    else:
      print(f"{self.ime}, dovolj si star, da se starši ne bodo jezili nad oceno!")

class Temnopolti(Clovek):
  def __init__(self, ime, lakota, stevilo_las):
    Clovek.__init__(self, ime, lakota, stevilo_las)
    self.lakota = lakota
    # if stevilo_las != type(1):
    #   raise Exception("število las mora biti številskega tipa!")
  
  def __str__(self):  # lahko sprejme samo self
    return f"{self.ime}: lakota = {self.lakota}, število las = {self.stevilo_las}"
  
  def verjetnost(self):
    if self.stevilo_las > 50000:
      if self.lakota == "True":
        print("Verjetno si boš naročil pohanega piščanca!")
      else:
        print("Verjetnost, da boš v prihodnjem tednu jedel piščanca, je velika!")
    else: 
      print(f"{self.ime}, čeprav si temnopolti, si vseeno plešast!")
    
print("osnovno:")
Luka = Clovek("Luka", 23, 40000)
print(Luka)
Luka.plesast()
Luka.smrt()
print("")

Eva = Clovek("Eva", 45, 100000)
print(Eva)
Eva.plesast()
Eva.smrt()
print("")

print("azijca:")
Lan = Azijec("Lan", 18, 4)
print(Lan)
Lan.klofuta()
print("")

Jana = Azijec("Jana", 34, 10)
print(Jana)
Jana.klofuta()
print("")

print("temnopolta:")
Joe = Temnopolti("Joe", True, 120000)
print(Joe)
Joe.verjetnost()
print("")

Mike = Temnopolti("Mike", False, 40000)
print(Mike)
Mike.verjetnost()
print("")
