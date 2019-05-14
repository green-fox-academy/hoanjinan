def a():
    b()

def b():
    c()

def c():
    raise TypeError

# This is a "very"*1000 bad and practice
try:
    a()
except:
    pass