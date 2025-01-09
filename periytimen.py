# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
#----------------------
#pystyy joko kokonaan importtaamaan toisista fileista asioita
# import oliot # Tuo koko oliot.py moduulin sisältö
import datetime
from oliot import Student # tuo vain student pohjan oliot moduulista

  #  Tuodaan oliot moduulista luokka

# YLILUOKKA ELI ÄITILUOKKA
# ==========================

class Person():
    """common class for all person in Raseko
    """
    
    def __init__(self, etunimi: str, sukunimi: str,):
        """creates a person ogject

        Args:
            etunimi (str): A first name
            sukunimi (str): A last name
        """
        self.etunimi = etunimi
        self.sukunimi = sukunimi

@staticmethod
def calculateAge(birthday) -> float:
    birthDay = datetime.datetime.fromisoformat(birthday)
    age = datetime.datetime.now() - birthDay
    ageInYears = age.days / 365
    return round(ageInYears)


@classmethod
def calculateAge2(cls, birthday):
    birthDay = datetime.datetime.fromisoformat(birthday)
    age = datetime.datetime.now() - birthDay
    ageInYears = age.days / 365
    return round(ageInYears)


# ALILUOKKA ELI LAPSILUOKKA

class RasekoStudent(Person):
    """the student class, inyherist person class
    """
    def __init__(self, etunimi: str, sukunimi: str, opiskelijanumero: str):
        """creates student object

        Args:
            etunimi (str): opiskelijan etunimi
            sukunimi (str): opiskelijan sukunimi
            opiskelijanumero (str): opiskelijanumero
        """
        super().__init__(etunimi, sukunimi) # Määritellään tapahtuvaksi yliluoka mukaan
        self.opiskelijanumero = opiskelijanumero # Ei määritelty yliluokassa

class RasekoTeacher(Person):
    """creates teacher object
    """
    def __init__(self, etunimi: str, sukunimi: str, luokat: list[str]):
        """

        Args:
            etunimi (str): Teachers first name
            sukunimi (str): Teachers last name
            luokat (list[str]): Teachers classes
        """
        super().__init__(etunimi, sukunimi,)
        self.luokat = luokat


if __name__ == "__main__":
    rasekoStudent = RasekoStudent("Jonne", "Janttari", "546736")
    print(f"Opiskelijan sukunimi on {rasekoStudent.sukunimi}.")
    
    luokat = ["TiVi23A", "TiVi23B", "TiVi20oa"]
    rasekoTeacher = RasekoTeacher("Markku", "Kynsihärvi", "Tivi20oa")
    
    print(f"{rasekoTeacher.etunimi}, opettaa ryhmiä {rasekoTeacher.luokat}")
    
    student = Student("Tuittu Kiukkunen", "auto22b", 2004-10-23)
    print (f"{student.name} on {student.calculateAge} ")