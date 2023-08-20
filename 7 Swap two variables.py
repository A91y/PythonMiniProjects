# Write a Python program to swap two variables.

a : int = int(input("Enter the first number: "))
b : int = int(input("Enter the second number: "))
print(f"Before swapping a = {a} and b = {b}")
temp : int = a
a = b
b = temp
print(f"After swapping a = {a} and b = {b}")

