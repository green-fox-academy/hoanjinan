import random
class Pirate():
    def __init__(self, count = 0, isDead = False):
        self.count = count
        self.isDead = isDead

    def drink_some_rum(self):
        self.count += 1

    def hows_it_going_mate(self):
        if self.count <= 4:
            print("Pour me anudder!!!!!")
            print(self.isDead)
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.isDead = True
            print(self.isDead)

    def die(self):
        self.isDead = True

    def brawl(self, enemy = False):
        self.enemy = enemy
        dice = random.randint(1, 3)
        if dice == 1:
            self.enemy = True
        elif dice == 2:
            self.isDead = True
        elif dice == 3:
            self.enemy = True
            self.isDead = True

pirate = Pirate()
pirate.drink_some_rum()
pirate.hows_it_going_mate()
pirate.drink_some_rum()
pirate.hows_it_going_mate()
pirate.drink_some_rum()
pirate.drink_some_rum()
pirate.hows_it_going_mate()
pirate.drink_some_rum()
pirate.hows_it_going_mate()

class Ship():
    def __init__(self, captain, pirates):
        self.captain = captain
        self.pirates = pirates
    
    def fill_ship(self):
        if self.captain >= 1:
            print("Captain is already assigned")
        else:
            pass