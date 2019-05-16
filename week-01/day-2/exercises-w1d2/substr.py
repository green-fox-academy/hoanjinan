#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one

def substr(str, keyword):
    count = 0
    word = ""
    for i in str:
        # word = ""
        count += 1
        for j in keyword:
            if i == j:
                word += j
                # print(word)
        if i == " ":
            if word == keyword:
                return count - len(keyword) - 1
            else:
                word = ""
    return -1

#  Example
# should print: `17`
print(substr("this is what I'm searching in", "searching"))

# should print: `-1`
print(substr("this is what I'm searching in", "not"))