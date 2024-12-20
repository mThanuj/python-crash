# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def printName(self):
#         print(self.fname, self.lname)
#
#
# class Student(Person):
#     def study(self):
#         print(f"{self.fname + ' ' + self.lname} is studying...")
#
#
# person = Person("john", "doe")
# person.printName()
#
# student = Student("M", "Thanuj")
# student.printName()
# student.study()

# # Single and Hierarchial
# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} makes a sound")
#
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} is barking")
#
#
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} is meowing")
#
#
# animal = Animal("General")
# animal.speak()
#
# cat = Cat("cat")
# cat.speak()


# # Multiple
# class LandAnimal:
#     def walk(self):
#         print("Walking")
#
#
# class WaterAnimal:
#     def swim(self):
#         print("Swimming")
#
#
# class Amphibian(LandAnimal, WaterAnimal):
#     pass
#
#
# amphibian = Amphibian()
# amphibian.swim()
# amphibian.walk()


# # Multi-level
# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name
#
#
# class Mammal(Animal):
#     def has_fur(self):
#         return True
#
#
# class Cat(Mammal):
#     def speak(self):
#         print("Meow")
#
#
# cat = Cat("Cat")
# cat.speak()
