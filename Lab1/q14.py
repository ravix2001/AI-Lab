# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

import os

os.system('cls')

class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = int(input("Enter the radius of a circle : "))

circle = Circle(r)

print(f"The area of circle is : {circle.area()}")

print(f"The perimeter of circle is : {circle.perimeter()}") 