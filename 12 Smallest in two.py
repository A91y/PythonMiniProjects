# Write a Python program to find the smallest number between the two numbers using different methods.

a : int = int(input("Enter first number: "))
b : int = int(input("Enter second number: "))

print(a if a<b else b, "is smaller by Method 1")

print((b, a)[a<b], "is smaller by Method 2 (Tuple Method)")

print({True: a, False: b}[a<b], "is smaller by Method 3 (Dictionary Method)")

print((lambda: b, lambda: a)[a<b](), "is smaller by Method 4 (Lambda Method)")
