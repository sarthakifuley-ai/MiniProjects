def calculate_tax(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    else:
        tax = 12500 + (income - 500000) * 0.20
    return tax
income = float(input("Enter Annual Income: ₹"))
tax = calculate_tax(income)
print(f"Income Tax = ₹{tax:.2f}")
print(f"Net Income = ₹{income - tax:.2f}")