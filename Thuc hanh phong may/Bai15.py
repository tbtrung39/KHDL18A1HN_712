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
danh_sach_le_binh_phuong = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, danh_sach)))
print("List ban đầu:", danh_sach)
print("List bình phương của các số lẻ:", danh_sach_le_binh_phuong)