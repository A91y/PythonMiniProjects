# Write a Python Program to find the area of triangle using Heron's Formula.


from math import sqrt
side1 : float = float(input("Enter the first side of the triangle: "))
side2 : float = float(input("Enter the second side of the triangle: "))
side3 : float = float(input("Enter the third side of the triangle: "))
s : float = (side1 + side2 + side3) / 2
area : float = sqrt(s * (s - side1) * (s - side2) * (s - side3))
print(f"Area of the triangle is {area}")
