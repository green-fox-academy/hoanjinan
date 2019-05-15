import csv

sort_list = []
f = open("movies.csv", "r")
#store the content from a file and eliminate ; from csv file
content = csv.reader(f, delimiter = ";")
#loop through all content and find the name and the year of the films and store in a 2d list
for i in content:
    sort_list.append([i[0], i[1]])
#sort the 2d list based on the second column which is the index of 1
sort_list.sort(key = lambda x: x[1])
print(f"The oldest film is: {sort_list[0][0]} released in {sort_list[0][1]}")
f.close()