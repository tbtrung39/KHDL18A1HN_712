n = int(input("Nhập số sinh vien:"))
ds_sinh_vien = []
for _ in range(n):
    ma_sv = int(input("Nhập mã sinh viên (6 ký tu):"))
    ten_sv = input("nhập tên sinh viên :")
    diem = float(input("nhập điểm sinh viên:"))
    diem = round(diem)
    ds_sinh_vien.append([ma_sv, ten_sv, diem])
ds_sinh_vien.sort(key = lambda   sv: sv[2], reversed = True)
print("\n Danh sách sinh viên sau sắp xếp")
for sv in ds_sinh_vien:
    print(f"{sv[0]}-{sv[1]}-{sv[2]}")
