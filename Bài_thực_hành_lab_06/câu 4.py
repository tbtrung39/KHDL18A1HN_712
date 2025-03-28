danh_sach = []
while True:
    so = int(input("Nhập số (0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)
# Chuyển số dương lên đầu
so_duong = [x for x in danh_sach if x > 0]
so_khong_duong = [x for x in danh_sach if x <= 0]
ds_moi = so_duong + so_khong_duong
print("Danh sách sau khi chuyển:", ds_moi)


# Chèn [1,2,3] vào các vị trí
# Chèn đầu
chen_dau = [1, 2, 3] + ds_moi.copy()
# Chèn cuối
chen_cuoi = ds_moi.copy() + [1, 2, 3]
# Chèn vị trí thứ 5
chen_vi_tri_5 = ds_moi.copy()
if len(chen_vi_tri_5) >= 4:
    chen_vi_tri_5[4:4] = [1, 2, 3]
else:
    chen_vi_tri_5.extend([1, 2, 3])
    
print("Chèn đầu:", chen_dau)
print("Chèn cuối:", chen_cuoi)
print("Chèn vị trí 5:", chen_vi_tri_5)

# Xóa phần tử thứ k
k = int(input("Nhập vị trí cần xóa (từ 1): ")) - 1
if 0 <= k < len(ds_moi):
    del ds_moi[k]
    print("Danh sách sau khi xóa:", ds_moi)
else:
    print("Vị trí không hợp lệ")

print("Tăng dần:", sorted(ds_moi))
print("Giảm dần:", sorted(ds_moi, reverse=True))