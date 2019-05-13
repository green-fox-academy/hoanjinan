class Sharpie():
    def __init__(self, colour, width):
        self.colour = colour
        self.width = width
        self.ink_amount = 100.0

    def use(self):
        self.ink_amount -= 3.14

sharp = Sharpie("blue", 56)
print(f"colour: {sharp.colour}, width: {sharp.width}, ink amount:{sharp.ink_amount}")
sharp.use()
print(f"colour: {sharp.colour}, width: {sharp.width}, ink amount:{sharp.ink_amount}")