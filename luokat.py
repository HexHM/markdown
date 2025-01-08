# ---------------

#Luokat !!!class!!!
# test
# määritellään luokka henkilö, jossa on kaksi omaisuutta (property)
class henkil:
    etunim = "Erkki"
    sukunim = "esimerkki"

# luodaan luokasta olio ja muutetaan sen sukunimi-ominaisuuden arvoa
henkil1 = henkil()
henkil1.sukunim = "turtiainen"

print("Tämän henkilön etunimi on", henkil1.etunim, "ja sukunimi on", henkil1.sukunim)