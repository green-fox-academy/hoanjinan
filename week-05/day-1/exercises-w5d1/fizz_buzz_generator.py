def fizzbuzz_generator():
    num = 0
    while True:
        num += 1
        if num % 3 == 0 and num % 5 != 0:
            yield "Fizz"
        elif num % 5 == 0 and num % 3 != 0:
            yield "Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        else:
            yield num

fizzbuzz = fizzbuzz_generator()

for _ in range(100):
    print(next(fizzbuzz))