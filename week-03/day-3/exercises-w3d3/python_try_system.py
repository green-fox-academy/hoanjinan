
user = "hello"
pwd = "world"
f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-3/exercises-w3d3/users.txt", "r")
content = f.read().splitlines()
if user in content:
    print("The user is already registered!")
    f.close()
else:
    f.close()
    f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-3/exercises-w3d3/users.txt", "a+")
    f.writelines(f"{user}\n{pwd}\n")
    f.close()

#update the content of the file
f = open("/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-03/day-3/exercises-w3d3/users.txt", "r")
content = f.read().splitlines()
f.close()

print(content)

