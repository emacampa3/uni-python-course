from datetime import datetime, timedelta

dan = input("vnesi prvi dan zadnje menstruacije v formatu dd.mm.LLLL: ")

zadnja_menstruacija = datetime.strptime(dan, "%d.%m.%Y") # tipa čas
datum_poroda = zadnja_menstruacija + timedelta(weeks=40) # zadnji menstruaciji prištejemo 40 tednov, da dobimo čas poroda
datum_poroda_čas = datum_poroda.strftime("%d.%m.%Y")
print(f"porod pričakuj dne: {datum_poroda_čas}")
