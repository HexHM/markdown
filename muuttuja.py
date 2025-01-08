# esimerkkejä muuttujien käytöstä
# ===============================

# yksinkertaiset muuttujat

# merkkijono string

etunimi = "erkki" #str
ika = 36 #int
ytöaineiden_keskiarvo = 2.5 #float
valmistunut = False # totuusarvo boolena

print(etunimi, "sai keskiarvoksi ytö-aineista", ytöaineiden_keskiarvo)
print(etunimi, "on valmistunut", valmistunut)

#------------------------------------------
# Rakenteelliset muuttujat

nimilista = ["Jonne", "Jasmiina", "timppa"] #Lista !!!list!!!
print("Listassa ensimmäisenä on", nimilista[0]) #indeksissä 0 oleva arvo
maara = len(nimilista) # Listan jäsenten määrä selviää len komennolla
print("nimilistassa on ", maara, "ihmisiä")
lista = sorted(nimilista) #sorted komennolla voi laittaa muuntajaan/vaihtaa aakkosjärjestykseen
print("Aakkostettu lista on", lista)

nimilist = ["heikki", "henna", "henkka"] #Lista !!!list!!!
print("Listassa ensimmäisenä on", nimilista[0]) #indeksissä 0 oleva arvo
maara = len(nimilista) # Listan jäsenten määrä selviää len komennolla
print("nimilistassa on ", maara, "ihmisiä")
nimilist.sort()
print("Aakkostettu lista on", nimilist)

# ---------------------------------

pino = []
# listään pinoon !!!append!!! komennolla, Pino nostetaan pinon viimeinen
pino.append("lätty 1")
pino.append("lätty 2")
pino.append("lätty 3")
# otetaan pinosta !!!pop!!! otetaan pois viimeinen
print(pino.pop(), "maistui tosi hyvältä")
print(pino.pop(), "maistui hyvältää")
print(pino.pop(), "alkoi jo tehdä tiukkaa")

# luodaan tyhjä lista (jono)
jono = []
jono.append("asiakas 1")
jono.append("asiakas 2")
jono.append("asiakas 3")
#otetaan jonosta
print("palveluvuorossa on nyt", jono.pop(2))
print("palveluvuorossa on nyt", jono.pop(0))
print("Palveluvuorossa on nyt", jono.pop(0))

# ---------------------------------

# monikko
ryhmat = ("TiVi24A", "TiVi23B", "TiVi20oa") # Monikko !!!Tuple!!!
print("Meidän ryhmä on", ryhmat[2]) 
# ryhmat[2] = "tivi20ka" # yksittäistä jäsentä ei voi muuttaa
ryhmat = ("TiVi24A", "TiVi23B", "TiVi20ka") # koko tuplea voi muuttaa
print("Meidän uusi ryhmä on", ryhmat[2])

# -----------------------------------------

joukko = {"Tuittu", "Assi", "Calle"} # Joukko !!!set!!!
print("Ja Joukkoon kuuluvat", joukko) #jäseniin ei voi viitata indeksillä eikä arvoa muuttaa
joukko = {"Paavo", "Assi", "Calle"}
print("joukkoon kuuluu nyt", joukko)
# pring(joukko[2]) ei toimi, ei indeksiä

#   Sets are unordered.
#   Set elements are unique. Duplicate elements are not allowed.
#   A set itself may be modified, but the elements contained in the set must be of an immutable type.
# --------------------------

# Sanakirja !!!dict!!!
# voi olla eri tieto tyyppejä (str ja int) samassa kirjastossa
henkilotiedot = {"etunimi": "Jonne", "sukunimi": "nönnönnöö", "ika": 16}

opiskelija1 = {"etunimi": "Jonne", "sukunimi": "nönnönnöö", "ika": 16}
opiskelija2 = {"etunimi": "henna", "sukunimi": "hertta", "ika": 16}
opiskelija3 = {"etunimi": "eetu", "sukunimi": "herra", "ika": 16}

opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print("opiskelijalista on", opiskelijalista)

print("opiskelijan etunimi", henkilotiedot["etunimi"], "sukunimi on", henkilotiedot["sukunimi"], "ja ikä on", henkilotiedot["ika"])
uusi_opiskelika = {"etunimi": "Assi", "sukunimi": "Kalma", "ika": 65}
# lisätään uusi arvo olemassa olevaan listaan
opiskelijalista.append(uusi_opiskelika)

# otetaan opiskelijalistan ensimmäinen jäsen
print("listassa ensimmäisenä on", opiskelijalistaa.pop"
      print/" Ja viimeisönö on", opi)