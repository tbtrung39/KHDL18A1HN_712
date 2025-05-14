import Matranvuong

print('Nhập kích thước ma trận 3x3')
M = Matranvuong.nhap_ma_tran(3)

print('Ma trận ban đầu:')
for row in M:
    print(row)

transposed = Matranvuong.chuyen_vi(M)
print('Ma trận chuyển vị:')
for row in transposed:
    print(row)

print('Ma trận', 'có' if Matranvuong.doi_xung(M) else 'không', 'đối xứng')