# Write a Python program to find simple interest

principal : float = float(input("Enter the principal amount: "))
rate : float = float(input("Enter the rate of interest: "))
time : float = float(input("Enter the time in years: "))
simple_interest : float = (principal * rate * time) / 100
print(f"Simple interest is {simple_interest}")
