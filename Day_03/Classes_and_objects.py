# # class is a blueprint
# class Car:
#     x = 5
#
#
# innova = Car()
# print(innova.x)
#
# mustang = Car()
# mustang.x -= 1
# print(mustang.x)


# # __init__()
# # it is a constructor
# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def printDetails(self):
#         print("Name:", self.name)
#         print("Year:", self.year)
#
#
# mustang = Car("Mustang", 1983)
# mustang.printDetails()
#
# innova = Car("Innova", 2003)
# innova.printDetails()


# # __str__()
# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def __str__(self):
#         return f"Name: {self.name}\nYear: {self.year}"
#
#
# mustang = Car("Mustang", 1983)
# print(mustang)


# # use defined functions
# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def drive(self):
#         print("Driving...")
#
#     def __str__(self):
#         return f"Name: {self.name}\nYear: {self.year}"
#
#
# mustang = Car("Mustang", 1983)
# return_type = mustang.drive()
# print(return_type)


# # modifying
# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def changeName(self, name):
#         self.name = name
#
#     def drive(self):
#         print("Driving...")
#
#     def __str__(self):
#         return f"Name: {self.name}\nYear: {self.year}"
#
#
# mustang = Car("Mustang", 1983)
# mustang.changeName("GT")
# print(mustang)
