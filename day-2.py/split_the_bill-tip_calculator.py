'''
Write a program that take a total bill, and based on the
tip that was decided, prints out the amount each person should pay.
'''

print("Welcome to Tipster!")
bill = float(input("What was the total bill? \n"))
num_persons = int(input("How many people are splitting the bill? \n"))
tip_percentage = float(input("What percentage tip would you like to pay? \n"))

tip = tip_percentage / 100
split_bill = bill / num_persons
final_bill = bill * tip
bill_per_person = (final_bill / num_persons) + split_bill
print(f"Each person should pay ${bill_per_person:.2f}")
