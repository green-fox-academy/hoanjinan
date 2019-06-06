# We have bunnies standing in a line, numbered 1, 2, ...
# The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears, 
# because they each have a raised foot. 
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunnies_again(num_bunnies):
    if num_bunnies == 0:
        return 0
    else:
        if num_bunnies % 2 == 0:
            return 3 + bunnies_again(num_bunnies - 1)
        else:
            return 2 + bunnies_again(num_bunnies - 1)

print(bunnies_again(5))