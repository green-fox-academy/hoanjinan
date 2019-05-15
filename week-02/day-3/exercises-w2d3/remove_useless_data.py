import csv

sort_list = []
f = open("election.csv", "r")
#store the content from a file and eliminate , from csv file
content = csv.reader(f, delimiter = ",")
#loop through the content and check whether there is missing value in the file as well as appending values to a list
for i in content:
    if "" not in i and len(i) == 4:
        sort_list.append(i)
#print out a list line by line
for i in range(len(sort_list)):
    print(sort_list[i])
f.close()
# print("c" in "car")