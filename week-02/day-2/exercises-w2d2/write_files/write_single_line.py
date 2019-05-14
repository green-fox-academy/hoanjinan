# Write a function that is able to manipulate a file
# By writing your name into it as a single line
# The file should be named "my-file.txt"
# In case the program is unable to write the file,
# It should print the following error message: "Unable to write file: my-file.txt"

try:
    f = open("my-file.txt", "w")
    f.write("Zilan Huang")
    f.close()
except FileNotFoundError:
    print("Unable to write file: my-file.txt")
