A = [[1, 2],
     [3, 4],
     [4, 0]]

num = 5

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = A[i][j] * num

print(A)