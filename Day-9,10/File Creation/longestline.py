file = open("student.txt", "r")
lines = file.readlines()
longest_line = ""
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line
print("Longest line:")
print(longest_line)
file.close()