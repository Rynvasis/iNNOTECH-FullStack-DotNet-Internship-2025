
# ==============
#  Person Class
# ==============
from datetime import datetime

class Person:
    def __init__(self, name, country, birth_date_str):
        self.name = name
        self.country = country
        try:
            self.birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


# =================
# Testing the class
# =================

name = input("Enter name: ")
country = input("Enter country: ")

while True:
    birth_date_str = input("Enter birth date (YYYY-MM-DD): ")
    try:
        person = Person(name, country, birth_date_str)
        break
    except ValueError as e:
        print(e)


print("\nPerson Info")
print(f"Name    : {person.name}")
print(f"Country : {person.country}")
print(f"Age     : {person.get_age()} years")
