# FUNKTIOT
# ========

# Funktion, joka ei palauta arvoa eikä käytä argumentteja

def tervehdys():
    """prints hyvää huomenta on the screen
    """
    print("hyvää huomenta")
    
tervehdys()

# def-komento määrittää funktion myöhempää käyttöä varten

def toivotus(nimi, aika):
    """Greets user differently according to the time of day

    Args:
        nimi (str): user's name
        aika (int): hour in military format
    """
    if aika > 16:
        viesti = f"hyvää iltaa {nimi}!"
    elif aika > 10:
        viesti = f"hyvää päivää {nimi}!"
    else:
        viesti = f"hyvää huomenta {nimi}!"

    print(viesti)
    
toivotus("heikki", 12)
# normaali koodi on globaali ja sitä voi käyttää def-komennon sisällä
alkuLitania = "Milloin minä olisin työt tehny"

def tyoMotivaatio(paiva: str) -> str:
    """returns the motto of day in finnish

    Args:
        paiva (str): weekday name ion Finnish

    Returns:
        str: The motto of the day
    """
    # Funktion sisällä oleva on local/def sisällä oleva muuttuja
    motto = {"maanantai": "na en malttanut", "tiistai": "na en tietänyt",
            "keskiviikko": "na en kerennyt",
            "torstai": "na en tohtinut",
            "perjantai": "on paha päivä",
            "lauantai": "on pyhän aatto",
            "sunnuntai": "suuri juhla",}
    
    dailyMotto = f"{alkuLitania}, {paiva.capitalize()}{motto[paiva]}."
    return dailyMotto

print (tyoMotivaatio("torstai"))