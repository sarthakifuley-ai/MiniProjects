total_bill = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = (total_bill * tip_percentage) / 100
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / number_of_people

addition = total_bill + tip_amount
subtraction = total_with_tip - tip_amount
multiplication = total_bill * 2
division = total_with_tip / number_of_people
modulus = int(total_bill) % number_of_people

print("\nBILL SUMMARY")
print(f"Original Bill Amount : {round(total_bill, 2)}")
print(f"Tip Amount           : {round(tip_amount, 2)}")
print(f"Total With Tip       : {round(total_with_tip, 2)}")
print(f"Amount Per Person    : {round(amount_per_person, 2)}")

print("\nArithmetic Operators Used:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")