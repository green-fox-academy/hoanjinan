def fibonacci_generator():
    init_num = 0
    next_num = 1
    ans = 0
    while True:
        ans = init_num + next_num
        init_num = next_num
        next_num = ans
        yield ans

fibonacci = fibonacci_generator()

for _ in range(100):
    print(next(fibonacci))
        