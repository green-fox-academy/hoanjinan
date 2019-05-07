# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

num = 8
win = False
guess = int(input("Please guess a number: "))

while win == False:
    if guess == 8:
        print(f"You found the number: {num}")
        win = True
    else:
        guess = int(input("Please guess the number again: "))
    