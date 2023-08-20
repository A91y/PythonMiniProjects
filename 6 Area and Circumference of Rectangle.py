# Write a Python program to find the area and circumference of a rectangle.

length : float = float(input("Enter the length of the rectangle: "))
breadth : float = float(input("Enter the breadth of the rectangle: "))
area : float = length * breadth
circumference : float = 2 * (length + breadth)
print(f"Area of the rectangle is {area} and circumference is {circumference}")
