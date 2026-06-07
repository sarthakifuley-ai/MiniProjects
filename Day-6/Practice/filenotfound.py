filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Contents:")
        print(content)

except FileNotFoundError:
    print("Error: File does not exist.")