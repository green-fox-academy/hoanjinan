# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.

try:
    def write_multi_lines(path, word, number):
        f = open(path, "a")
        for _ in range(number):
            f.writelines(f"{word}\n")
        f.close()
except FileNotFoundError:
    print("Please check the file location!")

write_multi_lines("my-file.txt", 5, 5)