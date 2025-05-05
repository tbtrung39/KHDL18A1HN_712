import matranvuong

n = int(input("Nhap kich thuoc ma tran vuong N: "))
m = matranvuong.nhap_ma_tran(n)

print("\nMa tran vua nhap:")
matranvuong.in_ma_tran(m)

print("\nMa tran chuyen vi:")
mt_cv = matranvuong.chuyen_vi(m)
matranvuong.in_ma_tran(mt_cv)

if matranvuong.la_ma_tran_doi_xung(m):
    print("\nMa tran la ma tran doi xung.")
else:
    print("\nMa tran khong phai la ma tran doi xung.")
