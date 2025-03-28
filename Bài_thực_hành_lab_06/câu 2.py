n = int(input("Nhập số phần tử n: "))
danh_sach = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# Tìm phần tử lớn thứ 2 và vị trí
if len(danh_sach) < 2:
    print("Danh sách có ít hơn 2 phần tử")
else:
    # Loại bỏ trùng lặp và sắp xếp giảm dần
    ds_khong_trung = sorted(list(set(danh_sach)), reverse=True)
    if len(ds_khong_trung) >= 2:
        gia_tri_lon_thu_2 = ds_khong_trung[1]
        vi_tri = [i for i, x in enumerate(danh_sach) if x == gia_tri_lon_thu_2]
        print(f"Phần tử lớn thứ 2: {gia_tri_lon_thu_2}, tại vị trí: {vi_tri}")
    else:
        print("Không có phần tử lớn thứ 2")

# Đếm số dương liên tiếp dài nhất
do_dai_max = do_dai_hien_tai = 0
for so in danh_sach:
    if so > 0:
        do_dai_hien_tai += 1
        do_dai_max = max(do_dai_max, do_dai_hien_tai)
    else:
        do_dai_hien_tai = 0
print(f"Dãy số dương liên tiếp dài nhất: {do_dai_max}")

# Tìm tổng số dương liên tiếp lớn nhất
tong_max = tong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        tong_hien_tai += so
        tong_max = max(tong_max, tong_hien_tai)
    else:
        tong_hien_tai = 0
print(f"Tổng dãy số dương liên tiếp lớn nhất: {tong_max}")