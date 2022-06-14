

class Student:

    def __init__(self, last_name: str, first_name: str, group: int, birth_year: int, rating: int):
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.birth_year = birth_year
        self.rating = rating

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"{self.birth_year} group #{self.group} is №{self.rating}"
