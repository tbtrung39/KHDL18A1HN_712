# Cau 17.
n = int(input('Nhap so sinh vien: '))
danh_sach_sinh_vien = []

for _ in range(n):
    ma_sv = int(input('Nhap ma sinh vien (6 ky tu): '))
    ten_sv = input('Nhap ten sinh vien: ')
    diem = float(input('Nhap diem sinh vien: '))
    diem = round(diem)
    danh_sach_sinh_vien.append([ma_sv, ten_sv, diem])

danh_sach_sinh_vien.sort(key=lambda sv: sv[2], reverse=True)

print("\nDanh sach sinh vien sau sap xep: ")
for sv in danh_sach_sinh_vien:
    print(f"{sv[0]}-{sv[1]}-{sv[2]}")