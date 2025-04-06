n= int(input('nhap so sinh vien : '))
ds_sinh_vien =[]
for _ in range(n):
    ma_sv = int(input('nhap ma sinh vien (6 ky tu): '))
    ten_sv =input('nhap ten sinh vien : ')
    diem = float(input('nhap diem sinh vien : '))
    diem = round(diem)
    ds_sinh_vien.append([ma_sv, ten_sv, diem])
ds_sinh_vien.sort(key=lambda  sv: sv[2], reverse= True)
print("\n Danh sach sinh vien sau sap xep: ")
for sv in ds_sinh_vien:
    print(f"{sv[0]}-{sv[1]}-{sv[2]}")