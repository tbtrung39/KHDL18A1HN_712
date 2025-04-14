def tinh_gia_tri_bieu_thuc(n):
    return sum(i / (i + 1) for i in range(1, n + 1))

n = int(input("Nhập n: "))
print("Giá trị biểu thức:", tinh_gia_tri_bieu_thuc(n))