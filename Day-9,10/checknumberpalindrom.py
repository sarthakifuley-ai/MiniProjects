num = int(input("Enter the number: "))
palindrome = num
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10
if palindrome == reverse:
    print("Number is palindrome",palindrome,"palindrom is ",reverse)
else:
    print(palindrome,"is not palindrome")