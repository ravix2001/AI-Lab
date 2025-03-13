# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age

from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
    
    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

name = input("Enter the name : ")
country = input("Enter the country : ")
date_of_birth = input("Enter thd date of birth : ")
person = Person(name, country, date_of_birth)
print(f"{person.name} from {person.country} is {person.age()} years old.")
