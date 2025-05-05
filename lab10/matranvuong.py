def nhap_ma_tran(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Nhập phần tử [{i}][{j}]: ")))
        matrix.append(row)
    return matrix

def chuyen_vi(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def doi_xung(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
