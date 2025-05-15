def nhap_ma_tran(n):
    print(f"Nhập ma trận {n}x{n}:")
    matran = []
    for i in range(n):
        row = list(map(int, input(f"Hàng {i+1}: ").split()))
        while len(row) != n:
            print(f"Bạn phải nhập đúng {n} số!")
            row = list(map(int, input(f"Hàng {i+1} (nhập lại): ").split()))
        matran.append(row)
    return matran

def in_ma_tran(matran):
    for row in matran:
        print(" ".join(map(str, row)))

def chuyen_vi(matran):
    n = len(matran)
    return [[matran[j][i] for j in range(n)] for i in range(n)]

def la_doi_xung(matran):
    n = len(matran)
    for i in range(n):
        for j in range(n):
            if matran[i][j] != matran[j][i]:
                return False
    return True
