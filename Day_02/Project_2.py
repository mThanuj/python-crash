options = ["Add", "Delete", "View Cart", "Generate Bill"]
products = [("burger", 50000), ("pizza", 80000)]

items = {}

while True:
    for index, option in enumerate(options):
        print(f"{index + 1}: {option}")

    ip = input("Select an option: ")

    match ip:
        case "1":
            for index, product in enumerate(products):
                print(f"{index + 1}. {product[0]} {product[1]}")

            order = int(input("Enter order: "))
            quantity = int(input("Enter quantity: "))

            index = order - 1

            if index in items:
                items[index] = items[index] + quantity
            else:
                items[index] = quantity
        case "2":
            for item in items.keys():
                name = products[item][0]
                current_quantity = items[item]

                print(f"{item + 1}. {name} {current_quantity}")

            order = int(input("Enter order: "))
            quantity = int(input("Enter quantity: "))

            index = order - 1

            current_quantity = items[index]

            if current_quantity >= quantity:
                items[index] = items[index] - quantity
        case "3":
            for item in items.keys():
                name = products[item][0]
                current_quantity = items[item]

                print(f"{item + 1}. {name} {current_quantity}")
        case "4":
            i = 1
            for item in items.keys():
                name = products[item][0]
                current_quantity = items[item]
                price = products[item][1]
                item_price = current_quantity * price

                print(f"{i}. {name} {current_quantity} {price} {item_price}")
                i += 1
            break

print("Thank you for choosing our restaurant")
