options = ["Add", "Update (status)", "Delete", "View all tasks", "Exit"]
todos = {}
current_id = 1

while True:
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    ip = input("Select an option: ")

    match ip:
        case "1":
            description = input("Enter description: ")
            todo = {"description": description, "status": "pending"}
            todos[current_id] = todo
            current_id += 1
        case "2":
            id = int(input("Enter id: "))
            todos[id]["status"] = "completed"
        case "3":
            id = int(input("Enter id: "))
            todos.pop(id)
        case "4":
            for id in todos.keys():
                print(f"{id}:")
                print(f"\tDescription: {todos[id]['description']}")
                print(f"\tStatus: {todos[id]['status']}")
        case "5":
            break
        case _:
            print("Invalid")

print("Thank you for using the program")
