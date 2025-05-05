def nhap_ma_tran(N):
    print(f"Nhập ma trận {N}x{N}:")
    matran = []
    for i in range(N):
        dong = list(map(int, input(f"Nhập dòng {i+1} (cách nhau bởi dấu cách): ").split()))
        while len(dong) != N:
            print(f"Vui lòng nhập đúng {N} phần tử.")
            dong = list(map(int, input(f"Nhập lại dòng {i+1}: ").split()))
        matran.append(dong)
    return matran

def in_ma_tran(matran):
    print("Ma trận vừa nhập:")
    for dong in matran:
        print(" ".join(map(str, dong)))

def chuyen_vi(matran):
    N = len(matran)
    ma_tran_cv = [[matran[j][i] for j in range(N)] for i in range(N)]
    print("Ma trận chuyển vị:")
    for dong in ma_tran_cv:
        print(" ".join(map(str, dong)))
    return ma_tran_cv

def kiem_tra_doi_xung(matran):
    N = len(matran)
    for i in range(N):
        for j in range(N):
            if matran[i][j] != matran[j][i]:
                return False
    return True