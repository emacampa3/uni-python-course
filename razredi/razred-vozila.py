class vozilo():
  def __init__(self, kolesa = 4, osebe = 4):
    self.nosilnost = 750 # privzeta vrednost 
    self.kolesa = kolesa
    self.osebe = osebe
    self.poraba = 7
  
  def __lt__(prvi, drugi): # prvi je manjši od drugega (če bi primerjali porabo, bi znak spodaj obrnili: manjša poraba je boljša)
    return prvi.nosilnost < drugi.nosilnost # vrne True, če je prvi manjši od drugega
  
  def __gt__(prvi, drugi): 
    return prvi.nosilnost > drugi.nosilnost

  def __eq__(prvi, drugi): # equal
    return prvi.nosilnost == drugi.nosilnost
  
  def __ne__(prvi, drugi): # not equal
    return prvi.nosilnost != drugi.nosilnost


  def hupaj(self):
    if self.nosilnost < 200:
      print("bip bip")
    elif self.nosilnost < 500:
      print("biiip biiip")
    else:
      print("BOOOOOOOOP")

class motor(vozilo): # podrazred vozila: podeduje vse, lahko pa spremenimo
  def __init__(self, kolesa = 2, osebe = 2):
    self.nosilnost = 200
    self.kolesa = kolesa
    self.osebe = osebe
    self.poraba = 7


class tovornjak(vozilo):  # podrazred vozila: podeduje vse, lahko pa spremenimo
  def __init__(self, kolesa=6, osebe=3):
    self.nosilnost = 3500
    self.kolesa = kolesa
    self.osebe = osebe
    self.poraba = 7

# definicija/kreiranje objektov
ficko = vozilo()
ficko.nosilnost = 150
ficko.poraba = 4

ranger = vozilo()
ranger.poraba = 15

guzzi = vozilo(2) # 2 kolesi
guzzi.nosilnost = 160 # nosilnost

scania = tovornjak()

print(f"fičko ima {ficko.kolesa} koles")

# kličemo 
ficko.hupaj()
scania.hupaj()
guzzi.hupaj()
