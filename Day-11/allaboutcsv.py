import csv
file = open("student.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["RollNo", "Name", "Sub1", "Sub2", "Sub3", "Sub4"])
for i in range(10):
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    sub1 = int(input("Enter Subject 1 Marks: "))
    sub2 = int(input("Enter Subject 2 Marks: "))
    sub3 = int(input("Enter Subject 3 Marks: "))
    sub4 = int(input("Enter Subject 4 Marks: "))
    writer.writerow([roll, name, sub1, sub2, sub3, sub4])
file.close()
file = open("student.csv", "r")
reader = csv.reader(file)
print("\nStudent Records:")
for row in reader:
    print(row)
file.close()
file = open("student.csv", "r")
reader = csv.reader(file)
next(reader) 
highest_total = 0
highest_student = ""
grand_total = 0
student_count = 0
for row in reader:
    total = int(row[2]) + int(row[3]) + int(row[4]) + int(row[5])
    if total > highest_total:
        highest_total = total
        highest_student = row[1]
    grand_total += total
    student_count += 1
file.close()
average_marks = grand_total / student_count
print("\nHighest Scorer:")
print("Name:", highest_student)
print("Total Marks:", highest_total)
print("\nAverage Marks of All Students:")
print(average_marks)