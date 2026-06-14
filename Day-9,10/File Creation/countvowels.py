file = open("student.txt","r")
content = file.read()
vowel_count = 0
for letter in content:
    if letter in "aeiouAEIOU":
        vowel_count += 1
print(vowel_count)
file.close()