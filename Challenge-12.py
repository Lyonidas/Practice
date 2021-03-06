# Preston Hudson 12/4/19 Challenge 12 Written in Python


#3.

class Shape():

    def what_am_i(self):
        print("I am a shape.")

#1. Create Rectangle and Square classes with a method that calculates perimeter.

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return (self.length + self.width) * 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, new_size):
        self.side += new_size

square = Square(4)
rectangle = Rectangle(22, 5)
print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

#2. Define a method in square class that allows you to pass in a number that increases or decreases each of the sides.

#3. Create a class called shape.

rectangle.what_am_i()
square.what_am_i

#4. Create a Horse and rider class and use composition.

class Horse():
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

bill = Rider("Bill Stanley")
bob = Horse("Bob", "Mustang", bill)
print(bob.rider.name


#Completed
