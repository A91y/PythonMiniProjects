# Write a Python program to find compound interest

principal: float = float(input("Enter the principal amount: "))
rate: float = float(input("Enter the rate of interest: "))
time: float = float(input("Enter the time in years: "))

compound_interest = principal*(((1 + (rate/100))**time)-1)

print(f"Compount interest is {compound_interest}")