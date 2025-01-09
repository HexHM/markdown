# LUOKAT JA OLIOT
# ===============

# OLION MALLIT ELI LUOKAT
# =======================


# KIRJASTOT JA MODUULIT
# =====================

import datetime


class Student():
    """A class for student onject."""
    
    # Konstruktori-metodi eli olionmuodostin
    def __init__(self, name:str, group:str, dateOfBirth:str):  #rivi on construct, self on nimi, argunemtit on nimi/vuosi/ikä
        """Constructor for a student object

        Args:
            name (str): name of student
            group (str): groups name
            dateOfBirth (str): date of birth
        """
    
    
        # Luokan kengät joista tulee ogjektien ominaisuudet
        self.name = name
        self.group = group
        self.birthDay = dateOfBirth

    def sutendOf(self) -> None:
        """_summary_
        """
        memberInGroup = f"{self.name} opiskelee luokalla {self.group}"
        print(memberInGroup)


    def calculateAge(self) -> int:
        """Calculates student's current age in full years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(self.birthDay)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)

if __name__ == "__main__":
    student = Student("Jonne", "Auto23A", "2008-05-21")

    print(student.name, "on syntyny", student.birthDay)

    student2 = Student("Tuittu", "Tivi20oa", "1990-03-09")

    student2.sutendOf()

    print("ikä on", student2.calculateAge())

