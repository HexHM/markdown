# MUUTTUJAT MERKKIJONOSSA
# ======================

# sanakirjat

henkilö1 = {"etunimi": "tiina", "ika": 27}
henkilö2 = {"etunimi": "helmi", "ika": 33}
henkilö3 = {"etunimi": "Pekka", "ika": 9}

# pereinteinen ratkaisu
print(henkilö1["etunimi"]+'n', "ikä on", henkilö1["ika"], "vuotta")

# sama muotoiltuna merkkijonona,
# tapa saada hienommaksi/helpommaksi luettavaksi toisille

muotoiltu_merkkijono = f"{henkilö1["etunimi"]}n ikä on {henkilö1["ika"]} vuotta"
print(muotoiltu_merkkijono)