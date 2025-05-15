n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    while True:
        try:
            so = int(input(f"Nhập phần tử thứ {i+1}: "))
            danh_sach.append(so)
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
danh_sach_binh_phuong = list(map(lambda x: x**2, danh_sach))
print("List ban đầu:", danh_sach)
print("List bình phương:", danh_sach_binh_phuong)