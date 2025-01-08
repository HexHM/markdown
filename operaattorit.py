# OPERAATTORIT JA VALINTARAKENTEET
#==================================
# Oppivelvollinen, jos alle 18 v

ika = 18

if ika < 18:
    print("Opiskelija on oppivelvollinen")

else: 
    print("Ei ole pakko tulla kouluun")

henkilö1 = {"etunimi": "tiina", "ika": 27}
henkilö2 = {"etunimi": "helmi", "ika": 33}
henkilö3 = {"etunimi": "Pekka", "ika": 9}



ika = henkilö2["ika"]
etunimi = henkilö2["etunimi"]


if ika > 12 and ika < 30:
    print( etunimi, "kuuluunuorisoon")

elif ika < 13:
    print(etunimi, "on kapsi")
else:
    print(etunimi, "on aikuinne")

# henkilö lasketaan nuorisoon 13 - 30

# vaihtoehtoinen ratkaisu
if ika >= 30:
    print("Tervetuloa aikuiseksi", etunimi)
elif ika >= 13:
    print("Olet nuorisohuligaani", etunimi)
else:
    print("Olet pahainen kakara", etunimi)

# Paljon vaihtoehtoja sisältävä ehtorakenne


sisalto = {"ohjelmointi": "kehitysympäristö ja ohjelmointikielet", 
           "ohjelmistokehittäjänä toimiminen": "projektityöskentely, tietovarastot, versiointi ja julkaisu",
           "komponenttikirjasto": "django, node.js, qt ja muut kirjastot", 
           "sulautetut järjestelmät": "c-ohjelmointi, Arduino ja raspberry Pi"}

while True:
  kysymys = input("minkä tutkinnon osan sisällön haluat nähdä ")
  if kysymys == "":
      break
  try:
        vastaus = sisalto[kysymys]
  except Exception as e:
        vastaus = "ei semmoista tutkinnon osaa ole olemassa"

  print(vastaus)


