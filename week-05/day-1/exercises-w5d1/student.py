from collections import namedtuple
from functools import reduce

Student = namedtuple("Student", "name age gender grades")

s1 = Student(name = "John", age = 16, gender = "male", grades = [5, 5, 4, 2])
s2 = Student(name = "Jane", age = 15, gender = "female", grades = [4, 3, 4, 4, 5])
s3 = Student(name = "Bob", age = 17, gender = "male", grades = [2, 2, 3, 1])

students = (s1, s2, s3)
# print(students)
# print(s1.name)

# Create a new list that only includes the boys
boys_only = list(filter(lambda stu: stu.gender == "male", students))
print(boys_only)

# Create a new list that only includes who's name starts with the letter J
name_j = list(filter(lambda stu: stu.name.startswith("J"), students))
print(name_j)

# Create a new list that only includes the girls
girls_only = list(filter(lambda stu: stu.gender == "female", students))
print(girls_only)

# Create a new list that only includes who's grade average is above 4
grade_avg = list(filter(lambda stu: sum(stu.grades) / len(stu.grades) >= 4, students))
print(grade_avg)

# Create a new list that only includes the boys who's name starts with the letter J
name_j_boy = list(filter(lambda stu: stu.name.startswith("J") and stu.gender == "male", students))
print(name_j_boy)

# Create a new list that only includes the girls who's grade average is above 4
girl_above_4 = list(filter(lambda stu: sum(stu.grades) / len(stu.grades) >= 4 and stu.gender == "female", students))
print(girl_above_4)

# Create a new list that only includes who's at least two 5s
two_5s = list(filter(lambda stu: stu.grades.count(5) >= 2, students))
print(two_5s)

# Create a new list that only includes who's grade average is above 4 and at at least got two 5s
above_4_two_5s = list(filter(lambda stu: sum(stu.grades) / len(stu.grades) >= 4 and stu.grades.count(5) >= 2, students))
print(above_4_two_5s)