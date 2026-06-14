list = [1,2,3,4,5,6,7,8,9,10]
even_count = 0
for i in list:
    if i%2 == 0:
        even_count += 1
        print(i)
print("Even count is : ",even_count)