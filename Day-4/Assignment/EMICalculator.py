def calculate_emi(principal, rate, years):
    r = rate / (12 * 100)
    n = years * 12
    emi = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return emi
principal = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))
emi = calculate_emi(principal, rate, years)
print(f"Monthly EMI = ₹{emi:.2f}")