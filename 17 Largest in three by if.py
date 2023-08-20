# Write a Python program to find the largest number between the three numbers using if statements.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))
c : int = int(input("Enter third number: "))

print("Largest is", end=" ")
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)