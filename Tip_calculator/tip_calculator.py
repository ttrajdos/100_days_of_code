print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

total = total + total * tip / 100
per_person_bill = total / people
print(f'Each person should pay {round(per_person_bill, 2):.2f}')