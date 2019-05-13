class Animal():
    def __init__(self, hunger = 50, thirst = 50):
        self.hunger = hunger
        self.thirst = thirst
    
    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

puppy = Animal()
puppy.eat()
puppy.drink()
print(f"{puppy.hunger} and {puppy.thirst}")
puppy.play()
print(f"{puppy.hunger} and {puppy.thirst}")