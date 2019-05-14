# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.


def count_lines(filename):
    try:
        f = open(filename)
        content = f.readlines()
        f.close()
        print(len(content))
    except FileNotFoundError:
        print("0")


count_lines("print_each_line.py")