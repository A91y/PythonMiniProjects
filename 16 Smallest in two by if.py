# Write a C program to find the smallest number between the two numbers using if statements.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))

print("Smallest is", end=" ")
if a<b:
    print(a)
else:
    print(b)
