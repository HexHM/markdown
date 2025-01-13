# PYTEST-TESTAUSFUNKTIOT
# ======================

# MODUULIEN JA KIRJASTOJEN LATAUKSET
# ==================================


# Käyttöjärjestelmän virheilmoitusten testaus vaatii pytest:n lataamisen
import pytest # jos et testaa virheilmoituksia, voi jättää pois

# Ladataa testattava moduuli
import periytimen

#luodaan testiolioita eri luokista testausta varten
person = periytimen.Person("Assi", "Kalma")

student = periytimen.RasekoStudent("Jonne", "Janttari", 20356)

teacher = periytimen.RasekoTeacher("Mikko", "Viljanen", "TiVi20oa",)


# TESTAUSFUNKTIO ELI YKSIKKÖTESTIT
# ================================

def test_person_properties():
    assert person.etunimi == "Assi"
    assert person.sukunimi == "Kalma"
    
def test_person_ag3():
    assert person.calculateAge3("2008-12-31") == 16
    
    def test_student_properties():
        assert student.oppilasnumero == 21313
        
     
    