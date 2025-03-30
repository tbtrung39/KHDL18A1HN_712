n = int(input("Nhập số phần tử: "))
danh_sach = tuple(int(input(f"Nhập số thứ {i+1}: ")) for i in range(n))
print(f"Số lớn nhất: {max(danh_sach)} ở vị trí {danh_sach.index(max(danh_sach))}")

max_positive_count = max_negative_count = count = 0
for num in danh_sach:
    if num > 0:
        count += 1
        max_positive_count = max(max_positive_count, count)
    else:
        count = 0
print(f"Số lượng số dương liên tiếp nhiều nhất: {max_positive_count}")

count = 0
for num in danh_sach:
    if num < 0:
        count += 1
        max_negative_count = max(max_negative_count, count)
    else:
        count = 0
print(f"Số lượng số âm liên tiếp nhiều nhất: {max_negative_count}")