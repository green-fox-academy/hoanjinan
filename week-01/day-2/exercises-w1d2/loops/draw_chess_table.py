# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

num = int(input("Please enter an integer number: "))
percent = "%"
space = " "
for i in range(0, num):
    if i % 2 == 0:
        print((percent + space) * num)
    else:
        print((space + percent) * num)