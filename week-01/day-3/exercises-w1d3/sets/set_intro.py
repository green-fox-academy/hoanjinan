my_set = set()

my_set.add("abcde")
my_set.add(1245)
my_set.add(3.141592654)
my_set.add(True)
my_set.add("Hello World!")

print(my_set)

my_set.discard("Hello World!")
my_set.discard(True)

print(my_set)

for i in my_set:
    print(i)

def check_rm_num(value):
    if value in my_set:
        my_set.remove(value)
        print(my_set)
    else:
        print(f"You dont have {value} in your set!")

check_rm_num(1245)

my_set.remove(42)