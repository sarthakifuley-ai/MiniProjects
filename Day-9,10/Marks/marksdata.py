file = open("marks.txt", "w")
for i in range(10):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    file.write(name + "," + str(marks) + "\n")
file.close()
file = open("marks.txt", "r")
print("\nStudents scoring more than 75:")
for line in file:
    data = line.strip().split(",")
    name = data[0]
    marks = int(data[1])
    if marks > 75:
        print(name, "-", marks)
file.close()