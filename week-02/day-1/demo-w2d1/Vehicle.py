class Vehicle:
    
    #counter = 0
    
    def __init__(self, kms):
        #Vehicle.counter += 1
        self.run_kms = kms

    def drive(self, kms):
        self.run_kms += kms

# v = Vehicle(0)
# v.drive(20)
# print(v.run_kms)