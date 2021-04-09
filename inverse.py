def inv(A):
    # Defining nXn matrix size as N
    N = len(A)
    # Creating identity matrix
    inverse = []
    for i in range(N):
        inverse.append([])
        for j in range(N):
            inverse[i].append(0)
        inverse[i][i] = 1
    # Making lower triangle zero
    for row in range(N):
        for c in range(N-row-1):
            if A[row][row] != 0:
                ratio = - A[row+c+1][row] / A[row][row]
                for col in range(N):
                    A[row+c+1][col] += A[row][col]*ratio
                    inverse[row+c+1][col] += inverse[row][col]*ratio
            else:
                temp = A[row]
                A[row] = A[row+1]
                A[row+1] = temp
    # Making upper triangle zero
    for row in range(N-1, -1, -1):
        for c in range(row):
            if A[row][row] != 0:
                ratio = - A[row-c-1][row] / A[row][row]
                for col in range(N):
                    A[row-c-1][col] += A[row][col]*ratio
                    inverse[row-c-1][col] += inverse[row][col]*ratio
            else:
                temp = A[row]
                A[row] = A[row-1]
                A[row-1] = temp
    # Making diagonals 1
    for row in range(N):
        ratio = 1/A[row][row]
        for col in range(N):
            A[row][col] *= ratio
            inverse[row][col] *= ratio
    # The returning A matrix will be identity matrix and inverse will be the
    # inverse of the matrix A.
    return inverse
