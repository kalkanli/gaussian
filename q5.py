# calculates the inverse of nxn matrix.
def get_inverse(matrix):
    determinant = calculate_determinant(matrix)
    adjoint = get_adjoint(matrix)
    for i in range(len(adjoint)):
        for j in range(len(adjoint)):
            adjoint[i][j] = round(adjoint[i][j] / determinant, 8)
    return adjoint

# calculate adjoint matrix of a size n by n
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

# it is used in order to find determinants.
# when one line and column has to be extracted 
# from the matrix this method is called
def divide_to_smaller_matrix(matrix, n, m):
    smaller_matrix = []
    for row in matrix[:m] + matrix[m+1:]:
        smaller_matrix.append(row[:n] + row[n+1:])
    return smaller_matrix

# calculates determinant
def calculate_determinant(matrix):
    if(len(matrix) == 2):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = 0
    coefficient = 1
    for i in range(len(matrix)):
        result = float(result + coefficient * matrix[0][i] * calculate_determinant(divide_to_smaller_matrix(matrix, i, 0)))
        coefficient = coefficient * -1
    return result

# prints 2 dimensional lists in matrix form
def print_m(matrix):
    for row in matrix:
        for element in row:
            s = "{:.5f}".format(element)
            if str(element)[0:1] != "-":
                s = " " + s
            print(s, end=" ")
        print()

def solve(filename):
    print('{}:'.format(filename))
    # get the content of a file
    Ab = []
    A = []
    f = open(filename, "r")
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        tokens = line.split(' ')
        Ab.append([float(token) for token in tokens])
        A.append([float(token) for token in tokens])

    # do the gaussian elimination
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
            for j in range(0, n):
                if j == row:
                    continue
                ratio = float(Ab[j][column] / Ab[row][column])
                for k in range(n+1):
                    Ab[j][k] = Ab[j][k] - Ab[row][k] * ratio
                    Ab[j][k] = round(Ab[j][k], 8)
            row = row + 1
            column = column + 1
    
    # finds and checks the rank of A and Ab, then performs the calculations accordingly
    result = []
    rank_of_A = 0
    rank_of_Ab = 0
    for i in range(n):
        if(Ab[i][i] != 0):
            rank_of_A += 1
        if(Ab[i][n] != 0):
            rank_of_Ab += 1
    
    if rank_of_Ab == rank_of_A == n: # rank(A) = n
        for i in range(n):
            result.append(round(Ab[i][n] / Ab[i][i], 8))
        print('Unique solution: ', end='')
        for x in result:
            print(x, end=' ')
        print()
        print("Inverted A: ")
        print_m(get_inverse(A))
    elif rank_of_A == rank_of_Ab < n: # rank(A) = rank(A|b) < n
        for i in range(rank_of_A):
            result.append(Ab[i][n] / Ab[i][i])
        while len(result) != n:
            result.append(0)
        print('Arbitrary variables: ', end='')
        for i in range(n):
            print('x{}'.format(i), end=' ')
        print()
        print('Arbitrary solution: ', end='')
        for i in range(n):
            print(result[i], end=' ')
        print()
    else: #If rank(A) < rank(A|b),
        print('Inconsistent problem')
    print()

solve("Data1.txt")
solve("Data2.txt")
solve("Data3.txt")
solve("Data4.txt")
solve("Data5.txt")