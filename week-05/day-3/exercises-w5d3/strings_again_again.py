# Given a string, compute recursively a new string where all the adjacent chars are now separated by a *

def strings_again_agian(string):
    if string == "":
        return string
    else:
        return string[:1] + "*" + strings_again_agian(string[1:])

string = "xbox"
print(strings_again_agian(string))