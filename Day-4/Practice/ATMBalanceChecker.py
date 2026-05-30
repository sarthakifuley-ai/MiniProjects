total_amout = 8000
withdraw_amount = input("Enter amount to withdraw: ")
def check_balance(balance):
    return total_amout - int(withdraw_amount) 
print(check_balance())