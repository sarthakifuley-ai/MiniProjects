inventory = {}
categories = set()


def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    inventory[pid] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }

    categories.add(category)
    print("✅ Product Added Successfully!")


def display_inventory():
    if not inventory:
        print("No products available.")
        return

    print("\n--- INVENTORY ---")
    print(f"{'ID':<10}{'Name':<15}{'Qty':<10}{'Price':<10}")
    print("-" * 45)

    for pid, product in inventory.items():
        print(f"{pid:<10}{product['name']:<15}{product['qty']:<10}{product['price']:<10}")


def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for pid, product in inventory.items():
        if pid.lower() == keyword or product["name"].lower() == keyword:
            print("\nProduct Found:")
            print(product)
            found = True

    if not found:
        print("❌ Product not found.")


def update_inventory():
    pid = input("Enter Product ID to update: ")

    if pid in inventory:
        inventory[pid]["qty"] = int(input("Enter New Quantity: "))
        inventory[pid]["price"] = float(input("Enter New Price: "))
        print("✅ Product Updated.")
    else:
        print("❌ Product not found.")


def delete_product():
    pid = input("Enter Product ID to delete: ")

    if pid in inventory:
        del inventory[pid]
        print("✅ Product Deleted.")
    else:
        print("❌ Product not found.")


def low_stock_alert():
    threshold = 10

    print("\n--- LOW STOCK PRODUCTS ---")
    found = False

    for pid, product in inventory.items():
        if product["qty"] < threshold:
            print(product["name"], "- Qty:", product["qty"])
            found = True

    if not found:
        print("No low stock items.")


def out_of_stock_alert():
    print("\n--- OUT OF STOCK PRODUCTS ---")
    found = False

    for pid, product in inventory.items():
        if product["qty"] == 0:
            print(product["name"])
            found = True

    if not found:
        print("No out-of-stock items.")


def inventory_report():
    total_items = len(inventory)
    total_value = 0

    for product in inventory.values():
        total_value += product["qty"] * product["price"]

    print("\n--- INVENTORY REPORT ---")
    print("Total Products:", total_items)
    print("Total Inventory Value: ₹", total_value)

    print("\nCategories:")
    for category in categories:
        print("-", category)


while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product")
    print("4. Update Inventory")
    print("5. Delete Product")
    print("6. Low Stock Alert")
    print("7. Out of Stock Alert")
    print("8. Inventory Report")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_inventory()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        low_stock_alert()

    elif choice == "7":
        out_of_stock_alert()

    elif choice == "8":
        inventory_report()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")