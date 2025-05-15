# Câu 18
m = int(input("Nhap so hang(m): "))
n = int(input("Nhap so cot(n): "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input("Nhap phan tu hang {}, cot {}: ".format(i+1, j+1)))
        hang.append(phan_tu)
    ma_tran.append(hang)
tong = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong += phan_tu
print("Ma tran da nhap:", ma_tran)
print("Tong cac phan tu cua ma tran:", tong)