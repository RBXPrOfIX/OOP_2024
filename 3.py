class Animal:
    def __init__(self, name, age, view):
        self.name = name
        self.age = age
        self.view = view

class Zebra(Animal):
    def description(self):
        return f"Zebra's name is {self.name}, and he is {self.age} years old, she is {self.view}."
class Dolphin(Animal):
    def description(self):
        return f"Dolphin's name is {self.name}, and he is {self.age} years, he is {self.view}."


zebra = Zebra("Carlos", "10", "colorful")
print(zebra.description())
dolphin = Dolphin("Doris", "7", "penguin killer")
print(dolphin.description())