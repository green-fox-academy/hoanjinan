class Apple():
    def get_apple(self, fruit):
        return fruit

class Sum():
    def __init__(self, num_list = [5, 3, 7, 2, 6]):
        self.num_list = num_list

    def total(self):
        sum_num = 0
        for i in self.num_list:
            sum_num += i
        return sum_num

class Anagram():
    def check_anagram(self, string_1, string_2):
        if sorted(string_1) == sorted(string_2):
            return True
        else:
            return False

class CountLetters():
    def count(self, value):
        counter = {}
        for letter in value:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
        return counter

# A simple test to debug if there are any bugs in it
# count = CountLetters()
# print(count.count_letters("letters"))

class Fibonacci():
    def fibonacci_calculator(self, num_index, range_index):
        next_num = num_index
        init_num = 0
        ans = 0
        for _ in range(range_index - 1):
            ans = init_num + next_num
            init_num = next_num
            next_num = ans
        return ans

# fibonacci = Fibonacci()
# print(fibonacci.fibonacci_calculator(1, 5))