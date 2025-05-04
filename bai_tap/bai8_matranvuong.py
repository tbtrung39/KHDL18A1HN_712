# matranvuong.py

def nhap_matran(n):
    mat = []
    for i in range(n):
        row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
        mat.append(row)
    return mat

def xuat_matran(mat):
    for row in mat:
        print(" ".join(map(str, row)))

def chuyen_vi(mat):
    return list(map(list, zip(*mat)))

def la_ma_tran_doi_xung(mat):
    return mat == chuyen_vi(mat)
