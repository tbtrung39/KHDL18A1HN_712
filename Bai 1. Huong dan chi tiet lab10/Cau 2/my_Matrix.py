def isMatrix(A):
    for row in A:
        if len(row) != len(A[0]):
            return False
    return True
def inMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=' ')
        print()
def isSquare(A):
    return isMatrix(A) and len(A) == len(A[0])
def changeRow(A, i, j):
    if not isMatrix(A) or i >= len(A) or j >= len(A):
        return False
    A[i], A[j] = A[j], A[i]
    return True
def changeColumn(A, i, j):
    if not isMatrix(A) or i >= len(A[0]) or j >= len(A[0]):
        return False
    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]
    return True
def Transpose(A):
    if not isSquare(A):
        return None
    n = len(A)
    AT = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            AT[i][j] = A[j][i]
    return AT
def getSymetry(A):
    if Transpose(A) == A:
        return True
    else:
        return False
