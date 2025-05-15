import Matranvuong

N = int(input("Nhập kích thước N của ma trận vuông: "))

matran = Matranvuong.nhap_ma_tran(N)

Matranvuong.in_ma_tran(matran)

Matranvuong.chuyen_vi(matran)

if Matranvuong.kiem_tra_doi_xung(matran):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")