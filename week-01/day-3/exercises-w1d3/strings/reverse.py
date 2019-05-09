# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string

def reverse(value):
    new_string = ""
    for i in range(len(value)):
        new_string = value[i] + new_string
    return new_string

reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(reversed))