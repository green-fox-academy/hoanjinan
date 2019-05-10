A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

def dimension_checker(mat_A, mat_B):
    if len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0]):
        pass
    else:
        print("Please check the dimension of your matrices!")
        exit()

def matrix_add(mat_A, mat_B):
    dimension_checker(mat_A, mat_B)
    mat_C = []

    for i in range(len(mat_A)):
        mat_C.append([0])
        for j in range(len(mat_A[0])):
            if j < len(mat_A[0]) - 1:
                mat_C[i].extend([0])
            mat_C[i][j] = mat_A[i][j] - mat_B[i][j]
    return mat_C

print(matrix_add(A, B))