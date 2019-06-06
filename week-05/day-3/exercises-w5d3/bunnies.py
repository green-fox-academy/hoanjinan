# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
# 2+2+2+2+2=10
def bunnies(num_bunnies):
    if num_bunnies == 0:
        return 0
    else:
        return 2 + bunnies(num_bunnies - 1)

print(bunnies(5))