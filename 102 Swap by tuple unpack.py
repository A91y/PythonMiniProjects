# Write a Python program to swap two variables using tuple unpacking.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))
print(f"Before swapping a = {a} and b = {b}")
a, b = b, a
print(f"After swapping a = {a} and b = {b}")
