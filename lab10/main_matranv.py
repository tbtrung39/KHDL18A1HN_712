import matranvuong

n = int(input("Nhập kích thước ma trận NxN: "))
mat = matranvuong.nhap_ma_tran(n)

print("Ma trận ban đầu:")
for row in mat:
    print(row)

transposed = matranvuong.chuyen_vi(mat)
print("Ma trận chuyển vị:")
for row in transposed:
    print(row)

print("Ma trận có đối xứng không?", "Có" if matranvuong.doi_xung(mat) else "Không")
