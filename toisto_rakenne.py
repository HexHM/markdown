# Toistorakenteet
#=================


# WHILE-SILMUKAT
#----------------


# Ikuinen silmukka
while True:
    print("pyorin ikusesti")
    poistu = input("haluatko jatkaa? K/e ")
    if poistu == "e":
        break # katkaiseesilmukan 

# Kierrosmääräinen silmukka
laskuri = 0
while laskuri < 10:
  print("nyt on menossa kierros", laskuri)
  laskuri += 1   # Tai laskuri = laskuri + 1 


# FOR-SILMUKAT
#--------------

# Rakenteellisen muuttujan arvojen läpikäynti
lista = ["Jonne", "tuittu", "Jakke", "Calle"]
for jasen in lista:
   print(jasen, "kuuluu listaan")
 

# Kierrosmääräinen silmukka

teksti = ""
for laskuri in range(10):
    teksti += "x"
    print("woohoo", teksti)

    # range-komento mahdollistaa alun, lopun ja askeleet

for parilliset_kymmenet in range(20,100,20):
    print(parilliset_kymmenet) 