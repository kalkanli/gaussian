def get_inverse(matrix):
    determinant = calculate_determinant(matrix)
    adjoint = get_adjoint(matrix)
    for i in range(len(adjoint)):
        for j in range(len(adjoint)):
            adjoint[i][j] = round(adjoint[i][j] / determinant, 8)
    return adjoint

def get_adjoint(matrix):
    if len(matrix) == 2:
        return [[matrix[1][1], -1*matrix[0][1]], [-1*matrix[1][0], matrix[0][0]]]
    transpose = []
    for i in range(len(matrix)):
        transpose.append([])
    cof1 = 1
    for i in range(len(matrix)):
        cof2 = cof1
        for j in range(len(matrix)):
            transpose[i].append(cof2 * calculate_determinant(divide_to_smaller_matrix(matrix, i, j)))
            cof2 = cof2 * -1
        cof1 = cof1*-1
    return transpose

def divide_to_smaller_matrix(matrix, n, m):
    smaller_matrix = []
    for row in matrix[:m] + matrix[m+1:]:
        smaller_matrix.append(row[:n] + row[n+1:])
    return smaller_matrix

def calculate_determinant(matrix):
    if(len(matrix) == 2):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = 0
    coefficient = 1
    for i in range(len(matrix)):
        result = float(result + coefficient * matrix[0][i] * calculate_determinant(divide_to_smaller_matrix(matrix, i, 0)))
        coefficient = coefficient * -1
    return result

def print_m(matrix):
    for row in matrix:
        print(row)

def solve(filename):
    Ab = []
    A = []
    b = []
    f = open(filename, "r")
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        tokens = line.split(' ')
        Ab.append([float(token) for token in tokens])
        b.append(float(tokens.pop()))
        A.append([float(token) for token in tokens])
    column = 0
    row = 0
    while row < n and column < n:
        pivot = -1
        for i in range(row, n):
            if Ab[i][column] != 0:
                pivot = i
        if pivot == -1:
            column = column + 1
            continue
        else:
            temp_row = Ab[row]
            Ab[row] = Ab[pivot]
            Ab[pivot] = temp_row
            for j in range(row + 1, n):
                ratio = float(Ab[j][column] / Ab[row][column])
                for k in range(n):
                    Ab[j][k] = Ab[j][k] - Ab[row][k] * ratio
                    Ab[j][k] = round(Ab[j][k], 8)
            row = row + 1
            column = column + 1
    result = []
    if row == column:
        inverted_matrix = get_inverse(A)
        for i in range(n):
            value = 0
            for j in range(n):
                value = value + b[j] * inverted_matrix[i][j]
            result.append(round(value, 8))
        print('Unique solution: ', end='')
        for x in result:
            print(x, end=' ')
        print()
        print("Inverted A: ")
        print_m(inverted_matrix)
    elif row > column:
        print('find arbitrary solution')
    else:
        print('Inconsistent problem')
    print()



solve("Data1.txt")
solve("Data2.txt")
solve("Data3.txt")
solve("Data4.txt")