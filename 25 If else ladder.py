# Write a Python program to find the value of y using if-else ladder.
#         1+x     n=1
#  y =    1+x/n   n=2
#         1+x^n    n=3
#         1+nx    otherwise

n: int = int(input("Enter n: "))
x: int = int(input("Enter x: "))
if n == 1:
    y = 1 + x
elif n == 2:
    y = 1 + x/n
elif n == 3:
    y = 1 + x**n
else:
    y = 1 + n*x
print("y = ", y)
