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

print("---------------------------------")

# luokka, johon on rakennettu muodostin ja metodi

class koodari:
    # Oliomuodostin, argumentteina etu- ja sukunimi, self viittaa luokasta luotavaan olioon
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
    
    # Metodi joka tulostaa ruudulle viestin
    def oma_kehu(self):
        print("mä oon", self.etunimi, "ja onn paras koodari ikinä")
# luodaan koodari1-olio muodostimella
koodari1 = koodari ("Jonne", "Janttari")

# Kutsutaan koodari1:n oma_kehu-meodia
koodari1.oma_kehu()