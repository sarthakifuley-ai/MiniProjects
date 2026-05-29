correct_password = "admin123"
for i in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
else:
    print("Account Blocked")