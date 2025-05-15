import Matranvuong
n=int(input("Nhap kich thuoc ma tran vuong: "))
matran=Matranvuong.nhapmatran(n)
Matranvuong.inmatran(matran)
print("\nMa tran chuyen vi: ")
machuyenvi=Matranvuong.chuyenvi(matran)
Matranvuong.inmatran(machuyenvi)
if Matranvuong.doixung(matran):
    print("\nMa tran doi xung")
else:
    print("\nMa tran khong doi xung")