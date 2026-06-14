file = open("student.txt","a")
for i in range(3):
    name = input("Enter name: ")
    file.write(name + "\n")
file.close()
