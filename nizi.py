# ord("a") # dobimo ASCII število 97
# chr(97) # dobimo črko "a"

# računa ujemanje dveh imen (glede na mesto v abecedi)
ime1 = input("vnesi prvo ime: ")
ime2 = input("vnesi drugo ime: ")

vsota = 0
crke = "abcčdefghijklmoprsštuvzž"

for crka in (ime1 + ime2): 
  if crka.lower() in crke:
    vsota += int(crke.index(crka)) + 1
    
    # če je vsota večja od 100, seštejemo prvi dve števili in dodamo število na 3. mestu
    if vsota > 100: 
      pretvorjeno = str(vsota)
      sestevek = str(int(pretvorjeno[0]) + int(pretvorjeno[1])) + pretvorjeno[2]

print(f"odstotek ujemanja: {sestevek} %")
