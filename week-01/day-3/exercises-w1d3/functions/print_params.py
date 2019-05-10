# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)

def print_params(*args):
    for i in args:
        print(i)

print_params(5, "egrwe", 2499)