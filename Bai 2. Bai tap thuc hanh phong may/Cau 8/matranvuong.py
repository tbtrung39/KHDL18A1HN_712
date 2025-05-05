def nhap_ma_tran(n):
    matran = []
    for i in range(n):
        dong = []
        for j in range(n):
            x = int(input(f"Nhap phan tu tai dong {i + 1}, cot {j + 1}: "))
            dong.append(x)
        matran.append(dong)
    return matran

def in_ma_tran(m):
    for dong in m:
        print(' '.join(str(x) for x in dong))

def chuyen_vi(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]

def la_ma_tran_doi_xung(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True
