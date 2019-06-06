# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def strings_again(string):
    if string == "":
        return string
    else:
        if string[0] == "x":
            return strings_again("" + string[1:])
        else:
            return string[:1] + strings_again(string[1:])

string = "xbox"
print(strings_again(string))