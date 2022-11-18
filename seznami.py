# list("abc") ["a", "b", "c"]
# list.append("d") doda na zadnje mesto
# list.insert(4, "e") na 5. mesto doda element "e"
# list.pop() izbriše zadnji element seznama (lahko vzame input)
# list.sort() sortira seznam, ki ima sama števila ali same besede: spremeni prvotni seznam
# new = sorted(list) naredi nov seznam, ki je sortirana verzija seznama list

# večina metod pri seznamih spreminja originalni seznam
# seznam = [1,2,["a","b",True,False],"stiri",[5,-5,0],2]
# print(seznam)
# seznam[2] # izpis 3. elementa
# seznam[1:3] # izpiše elementa 2 in 3
# del seznam[2] # izbrišemo 3. element
# seznam[4] = ["Ema", "Campa"] # 4. element zamenjamo z novim seznamom
# seznam[4][1:3] # dostop do števil -5 in 0


s = []

while True:
  x = input("vnesi številko ali \"Enter\" za konec: ")
  if x == "":
    break
  s.append(int(x)) # spremenimo v int, ko vemo, da x ni prazen niz (Enter)

print(s)
print(s.index(42)) # vrne index mesta, na katerem je število 42
del(s.index(42)) # izbriše index, na katerem je število 42
s.sort() # privzeto po naraščajoči vrednosti
s.sort(reverse=True) # razvrsti po padajoči vrednosti
s.reverse() # obrne vrstni red seznama


# seznam, ki se ga ne da spreminjati = TUPLE
tuple = (1, 2, 3, [4, 5]) # spreminjanje celega seznama znotraj tupla se ne da spremeniti, znotraj seznama pa se lahko spreminja elemente

# SET
s = {2, 3, 4, 4, 5} # notri so lahko le unikatni elementi, podvojeni se zbrišejo





