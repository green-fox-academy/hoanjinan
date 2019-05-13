from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, colour, brand):
        super().__init__(0)
        #Vehicle.__init__(self, 0)
        self.colour = colour
        self.brand = brand

    def __str__(self):
        return f"this is a {self.colour} {self.brand}"

my_car = Car("black", "mercedes")

my_car.drive(30)
print(my_car.run_kms)
print(my_car.brand)
print(my_car.colour)
print(my_car)

print(isinstance(my_car, Vehicle))
print(isinstance(my_car, float))