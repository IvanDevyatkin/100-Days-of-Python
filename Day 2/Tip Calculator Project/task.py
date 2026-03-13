print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_tip_amount = bill * (tip / 100)
final_bill = total_tip_amount + bill
final_bill_per_person = round(final_bill / people, 2)

print(f"Each person should pay ${final_bill_per_person}")


