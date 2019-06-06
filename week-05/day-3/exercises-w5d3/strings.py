# Given a string, compute recursively (no loops) a new string 
# where all the lowercase 'x' chars have been changed to 'y' chars.

def strings(string):
    if string == "":
        return string
    else:
        if string[0] == "x":
            return strings("y" + string[1:])
        else:
            return string[:1] + strings(string[1:])

string = "xbox"
print(strings(string))

# print(string[:2])
# print(string[0:])