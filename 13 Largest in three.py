# Write a Python program to find the largest number between the three numbers using different methods.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))
c : int = int(input("Enter third number: "))

print(a if a>c else c if a>b else b if b>c else c, "is larger by Method 1")

print(((c, b)[b>c], (c, a)[a>c])[a>b], "is larger by Method 2 (Tuple Method)")

print({True: {True: a, False: c}[a>c], False: {True: b, False: c}[b>c]}[a>b], "is larger by Method 3 (Dictionary Method)")

print((lambda: (lambda: c, lambda: b)[b>c](), lambda: (lambda: c, lambda: a)[a>c]())[a>b](), "is larger by Method 4 (Lambda Method)")
