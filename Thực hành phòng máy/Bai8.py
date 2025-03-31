danh_sach = input("Nhập danh sách các chuỗi, cách nhau bởi dấu phẩy: ").split(",")
# In ra danh sách ban đầu
print("\nDanh sách chuỗi ban đầu:", danh_sach)
dem = 0
for chuoi in danh_sach:
    chuoi = chuoi.strip()
    if len(chuoi) >= 2 and chuoi[0] == chuoi[-1]:
        dem += 1
print("\nSố lượng chuỗi thỏa mãn điều kiện:", dem)
danh_sach_khong_trung = list(set(danh_sach))

print("\nDanh sách sau khi loại bỏ phần tử trùng:", danh_sach_khong_trung)
