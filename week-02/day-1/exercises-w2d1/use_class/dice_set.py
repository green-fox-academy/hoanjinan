import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()

# examples:
# dice_set = DiceSet()
# print(dice_set.get_current())
# dice_set.roll()
# print(dice_set.get_current())
# dice_set.reroll(3)
# print(dice_set.get_current(3))
# print(dice_set.get_current())

dice_six = DiceSet()
dice_six.roll()
print(dice_six.get_current())
for i in range(len(dice_six.dices)):
    while dice_six.get_current(i) != 6: 
        dice_six.reroll(i)

print(dice_six.get_current())


