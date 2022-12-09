import random, os, time

# ukaz za izbris zaslona: Windows = cls, osX = clear
def brisi_zaslon():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

  return

# računalnik naključno izbere 10 črk, 
vse_crke = "abcčdefghijklmnoprsštuvzž"
izbrane = ""

# izpiše 10 naključnih črk (te se ne ponavljajo)
while len(izbrane) < 10:
  crka = random.choice(vse_crke)
  if crka not in izbrane:
    izbrane += crka


brisi_zaslon()

print(f"izbral sem tole: {izbrane}")

time.sleep(10) # čaka 10 sekund
brisi_zaslon()

ugibanje = input("ugani, kaj sem izbral: ")
stevec = 0
uganjene_crke = 0

for crka_ugibanje in ugibanje:
  if stevec > 9:
    break
  if crka_ugibanje in izbrane:
    uganjene_crke += 1
  stevec += 1

print(f"uganil si {uganjene_crke*10} % vseh")


# typewriter effect
besedilo = "danes je lep dan"
for a in besedilo:
  print(a, end="")
  time.sleep(0.2)
