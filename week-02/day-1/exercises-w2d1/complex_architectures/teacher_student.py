class Student():
    def __init__(self, ans = "how to do"):
        self.ans = ans

    def learn(self):
        teach = Teacher()
        teach.answer()

class Teacher():
    def __init__(self, ques = "multiply the number"):
        self.ques = ques

    def answer(self):
        stu = Student()
        stu.learn()
