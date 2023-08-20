# Write a Python program to calculate area and circumference of a circle.
from math import pi

radius : float = float(input("Enter the radius of the circle: "))
area : float = pi * radius * radius
circumference : float = 2 * pi * radius
print(f"Area of the circle is {area} and circumference is {circumference}")
