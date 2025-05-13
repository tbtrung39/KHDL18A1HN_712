def nhapmatran(n):
    print(f"Nhap ma tran {n}x{n}:")
    matran=[]
    for i in range(n):
        hang=list(map(int,input(f"Hang {i+1}: ").split()))
        while len(hang)!=n:
            print("So phan tu khong dung, nhap lai")
            hang=list(map(int,input(f"Hang {i+1}: ").split()))
            matran.append(hang)
    return matran

def inmatran(matran):
    print("Ma tran: ")
    for hang in matran:
        for hang in matran:
            print(" ".joint(map(str, hang)))

def chuyenvi(matran):
    n=len(matran)
    return [[matran[j][i] for j in range(n)]for i in range(n)]

def doixung(matran):
    n=len(matran)
    for i in range(n):
        for j in range(n):
            if matran[i][j] != matran[j][i]:
                return False
    return True