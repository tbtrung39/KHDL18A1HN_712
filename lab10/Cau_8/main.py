import matranvuong
n=int(input("Nhap kich thuoc ma tran vuong: "))
matran=matranvuong.nhapmatran(n)
matranvuong.inmatran(matran)
print("\nMa tran chuyen vi: ")
machuyenvi=matranvuong.chuyenvi(matran)
matranvuong.inmatran(machuyenvi)
if matranvuong.doixung(matran):
    print("\nMa tran doi xung")
else:
    print("\nMa tran khong doi xung")