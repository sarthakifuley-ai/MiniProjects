def simple_intrest(p,r,t):
    return (p*r*t)/100
principal = int(input("Enter the principal amount: "))
rate_of_intrest = float(input("Enter the rate of intrest: "))   
time = float(input("Enter the time in years: "))
print("The simple intrest is: ",simple_intrest(principal,rate_of_intrest,time))