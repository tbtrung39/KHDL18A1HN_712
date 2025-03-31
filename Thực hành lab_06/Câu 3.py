#Câu 3:
danh_sach = tuple(iter(lambda: int(input("Nhập số: ")), 0))
so_duong = tuple(x for x in danh_sach if x > 0)
print("Các số dương trong danh sách:", so_duong)

m = int(input("Nhập số m: "))
danh_sach = (m,) + danh_sach + (m,)
danh_sach = danh_sach[:5] + (m,) + danh_sach[5:]
print("Danh sách sau khi chèn m:", danh_sach)