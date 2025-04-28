#Câu 7:
def tim_nghiem(n, N, d=[]):
    if n == 0:
        if N == 0:
            print(d)
        return
    for i in range(N + 1):
        tim_nghiem(n-1, N - i, d + [i])
n = int(input("Nhap so luong phan tu n: "))
N = int(input("Nhap tong N: "))
print(f"Cac bo nghiem x1 + x2 + ... +x{n} = {N} la: ")
tim_nghiem(n , N)
