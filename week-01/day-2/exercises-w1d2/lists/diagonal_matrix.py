# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
num = int(input("Please specify a number: "))
two_d_array = []
for i in range(num):
    two_d_array.append(["0" * i + "1" + "0" * (num - i - 1)])

for i in range(len(two_d_array)):
    print(two_d_array[i][0])