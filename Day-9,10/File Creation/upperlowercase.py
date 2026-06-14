file = open("student.txt", "r")
content = file.read()
upper_case_content = 0
lower_case_content = 0
for letter in content:
    if letter.isupper():
        upper_case_content += 1
    elif letter.islower():
        lower_case_content += 1
print("Upper case letters: ", upper_case_content)
print("Lower case letters: ", lower_case_content)
file.close()