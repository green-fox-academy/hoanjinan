path = "/Users/hoanjinan_otoko/Desktop/epam-ds-training/greenfox/hoanjinan/week-02/day-2/demo-w2d2/error-handling.py"
f = open("error-handling.py")
content = f.readlines()
f.close()

print(type(content))
print(content)
print(len(content))

for line in content:
    print(line, end = "")

f = open("example-output", "a")
f.write("Hello\n")
f.close()

with open("example-output", "a") as f:
    f.write("Hello from with statement\n")