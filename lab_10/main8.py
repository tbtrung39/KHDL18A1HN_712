import Matranvuong

n = int(input("Nhập kích thước ma trận NxN: "))
mat = Matranvuong.nhap_ma_tran(n)

print("Ma trận ban đầu:")
for row in mat:
    print(row)

transposed = Matranvuong.chuyen_vi(mat)
print("Ma trận chuyển vị:")
for row in transposed:
    print(row)

print("Ma trận có đối xứng không?", "Có" if Matranvuong.doi_xung(mat) else "Không")