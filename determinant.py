def det(A):
    # Defining nXn matrix size as N
    N = len(A)
    # Making lower triangle zero
    for row in range(N):
        for c in range(N-row-1):
            if A[row][row] != 0:
                ratio = - A[row+c+1][row] / A[row][row]
                for col in range(N):
                    A[row+c+1][col] += A[row][col]*ratio
            else:
                temp = A[row]
                A[row] = A[row+1]
                A[row+1] = temp
    # Calculating determinant by multiplying each diagonal with themselves.
    determinant = 1
    for i in range(N):
        determinant *= A[i][i]
    return determinant
