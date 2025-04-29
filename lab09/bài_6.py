import random
def tao_hoan_vi_ngaunhien(n):
    A = list(range(1,n+1))
    ket_qua = []

    while A:
        vi_tri = random.randint(0 , len(A) -1 )
        phan_tu = A.pop(vi_tri)
        ket_qua.append(phan_tu)

    return ket_qua

n = int(input("Nhập số tự nhiên n : "))
hoan_vi_ngau_nhien = tao_hoan_vi_ngaunhien(n)
print("Hoán vị ngẫu nhiên : ",hoan_vi_ngau_nhien)