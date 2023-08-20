# Write a Python program to swap two variables without using third variable.

a : int = int(input("Enter the first number: "))
b : int = int(input("Enter the second number: "))
print(f"Before swapping a = {a} and b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping a = {a} and b = {b}")
