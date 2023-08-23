# Write a Python program to find the roots of a quadratic equation ax2+bx+c = 0 for all possible combination of a, b and c.

import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b**2 - 4*a*c
if d < 0:
    print("No Real Roots")
elif d == 0:
    print("Roots are: ", -b/(2*a))
else:
    print("Roots are: ", (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a))
