def even_odd(num):
    if num%2 == 0:
        return num,"is even"
    else:
        return num,"is odd"
number = int(input("Enter the number: "))
print(even_odd(number))