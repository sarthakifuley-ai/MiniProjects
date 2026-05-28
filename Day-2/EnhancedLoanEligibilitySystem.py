age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))
employment = input("Enter employment type (salaried/self-employed): ")

if age < 21:
    print("Rejected: Minimum age should be 21")

elif age > 60:
    print("Rejected: Maximum age limit is 60")

elif salary < 25000:
    print("Rejected: Salary should be at least ₹25,000")

elif employment not in ["salaried", "self-employed"]:
    print("Rejected: Invalid employment type")

elif 21 <= age <= 30 and salary < 30000:
    print("Needs guarantor")

elif age > 55 and employment == "self-employed":
    print("High risk, senior review needed")

else:
    print("Approved")