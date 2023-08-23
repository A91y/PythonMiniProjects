# Write a Python program to print the grade according to the marks secured by students.
#         Marks   Grade
#         >=90      A
#         >=80      B
#         >=70      C
#         >=60      D
#         otherwise F

physics = int(input("Enter Physics Marks: "))
chemistry = int(input("Enter Chemistry Marks: "))
maths = int(input("Enter Maths Marks: "))
total = physics + chemistry + maths
percentage = total / 3
print("Percentage: ", percentage)
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")
