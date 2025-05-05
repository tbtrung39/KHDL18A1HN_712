import matranvuong

N = int(input("Nhập kích thước N của ma trận vuông: "))

matran = matranvuong.nhap_ma_tran(N)

matranvuong.in_ma_tran(matran)

matranvuong.chuyen_vi(matran)

if matranvuong.kiem_tra_doi_xung(matran):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")