# Nhập danh sách
danh_sach = []
while True:
    so = int(input("Nhập số (dừng khi nhập 0): "))
    if so == 0:
        break
    danh_sach.append(so)

# Chuyển số dương lên đầu danh sách
danh_sach_duong = [x for x in danh_sach if x > 0]
danh_sach_am = [x for x in danh_sach if x <= 0]
danh_sach_moi = danh_sach_duong + danh_sach_am
print("Danh sách sau khi chuyển số dương lên đầu:", danh_sach_moi)

# Chèn số m vào các vị trí (tạo bản sao để mỗi lần chèn độc lập)
m = int(input("Nhập số m cần chèn: "))

# Danh sách chèn ở đầu
ds_dau = danh_sach_moi.copy()
ds_dau.insert(0, m)
print("Danh sách sau khi chèn vào đầu:", ds_dau)

# Danh sách chèn ở cuối
ds_cuoi = danh_sach_moi.copy()
ds_cuoi.append(m)
print("Danh sách sau khi chèn vào cuối:", ds_cuoi)

# Danh sách chèn ở vị trí thứ 5 (index 4)
ds_vitri5 = danh_sach_moi.copy()
if len(ds_vitri5) >= 4:
    ds_vitri5.insert(4, m)
else:
    ds_vitri5.append(m)
print("Danh sách sau khi chèn vào vị trí thứ 5:", ds_vitri5)