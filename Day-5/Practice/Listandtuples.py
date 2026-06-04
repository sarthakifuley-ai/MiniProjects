# 1. List of Fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruits:")
for fruit in fruits:
    print(fruit)

# 2. Tuple of Colors
colors = ("Red", "Blue", "Green")
print("\nFirst Color:", colors[0])

# 3. Dictionary of Students
students = {
    "Sarthaki": 85,
    "Stavya": 90,
    "Arush": 78
}
print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# 4. Set of Numbers
numbers = {10, 20, 30, 40, 50}
print("\nUnique Values:")
for num in numbers:
    print(num)

# 5. Product Stock Dictionary
stock = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}
print("\nStock Details:")
for product, quantity in stock.items():
    print(product, ":", quantity)