class Counter():
    def __init__(self, number = 0):
        self.number = number

    def add(self, number):
        self.number += number

    def get(self):
        return self.number
    
    def reset(self):
        self.number = 0