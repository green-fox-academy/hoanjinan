class Person():
    def __init__(self, name):
        self.name = name
        self.hunger = 10

    def greet(self, other):
        return f"Hello, {other.name}!"

    def is_hungry(self):
        return self.hunger > 5

    def eat(self, amount = 1):
        self.hunger -= amount
    
    def __str__(self):
        return f"I'm {self.name} and I'm{'' if self.is_hungry() else 'not'} hungry."