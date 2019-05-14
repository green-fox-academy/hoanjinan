# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

def divide(num):
    try:
        return 10 / num
    except ZeroDivisionError:
         print("0 cannot divide")



divide(0)