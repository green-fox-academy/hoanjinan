class Station():
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self):
        car = Car()
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity

class Car():
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity