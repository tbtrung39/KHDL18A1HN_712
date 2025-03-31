n = int(input("Nhập số phần tử n: "))
danh_sach = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
danh_sach_sap_xep = sorted(set(danh_sach), reverse=True)
if len(danh_sach_sap_xep) > 1:
    lon_thu_2 = danh_sach_sap_xep[1]
    vi_tri_lon_thu_2 = danh_sach.index(lon_thu_2)
    print(f"Phần tử lớn thứ hai là: {lon_thu_2}, vị trí: {vi_tri_lon_thu_2}")
else:
    print("Không có phần tử lớn thứ hai!")
max_dong_duong = 0
dem_dong_duong = 0
for so in danh_sach:
    if so > 0:
        dem_dong_duong += 1
        max_dong_duong = max(max_dong_duong, dem_dong_duong)
    else:
        dem_dong_duong = 0
print(f"Số lượng các số dương liên tiếp nhiều nhất: {max_dong_duong}")
max_tong = 0
tong = 0
dem_max_tong = 0
for so in danh_sach:
    if so > 0:
        tong += so
        dem_max_tong += 1
        max_tong = max(max_tong, tong)
    else:
        tong = 0
        dem_max_tong = 0
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất: {dem_max_tong}")
