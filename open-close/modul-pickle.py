import pickle

d = {"ime": "Ema", "priimek": "Čampa"}
print(d)

with open("oseba.pic", "wb") as f:
  pickle.dump(d, f)

del d

with open("oseba.pic", "rb") as f:
  d2 = pickle.load(f)
print(d2)
