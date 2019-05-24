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

class Farm():
    def __init__(self):
        puppy = Animal(20, 70)
        pig = Animal(90, 60)
        cat = Animal()
        self.animals = [puppy, pig, cat]
        self.places = 4
    
    def breed(self, hunger = 50, thirst = 50):
        if self.places > len(self.animals):
            self.animals.append(Animal(hunger, thirst))
            for i in self.animals:
                print(i.hunger)
        else:
            print("The breed is full!")

    def slaughter(self):
        max_hunger = self.animals[0].hunger
        for i in self.animals:
            if i.hunger > max_hunger:
                max_hunger = i.hunger

        for i in range(len(self.animals)):
            if self.animals[i].hunger == max_hunger:
                self.animals.pop(i)
                break
                
        for i in self.animals:
                print(i.hunger)

farm = Farm()
farm.breed(0, 0)
farm.breed(40, 40)
farm.slaughter()