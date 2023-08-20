# Write a Python program to swap two numbers using XOR.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))
print(f"Before swapping a = {a} and b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping a = {a} and b = {b}")
