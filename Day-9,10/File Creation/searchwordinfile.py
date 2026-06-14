file = open("student.txt","r")
word = input("Enter a word to search in file: ")
content = file.read()
if word in content:
    print(word,"is present in the file")
else:
    print(word,"not found in the file")
