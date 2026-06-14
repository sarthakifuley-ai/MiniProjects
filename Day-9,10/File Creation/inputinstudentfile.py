file = open("student.txt", "w")
for i in range(5):
    name = input(f"Enter student name {i+1}: ")
    file.write(name + "\n")

file.close()

print("Student names saved successfully.")