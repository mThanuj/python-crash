age = 18
nationality = "US"

if age == 18:
    print("Age: 18")
elif age < 18:
    print("Age less than 18")
else:
    print("Age greater than 18")
    if nationality == "Indian":
        print("Eligible for voting")

match age:
    case 18:
        print(18)
    case 19:
        print(19)
    case _:
        print("Other")
