list = ['a', 'e', 'i', 'o', 'u']
string = input("Enter a string: ")
vowel_count = 0
for char in string:
    if char.lower() in list:
        vowel_count += 1
print(vowel_count)
