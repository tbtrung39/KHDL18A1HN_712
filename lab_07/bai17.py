n= int(input('Nhap so sinh vien : '))
ds =[]
for _ in range(n):
    ma = int(input('Nhap ma sinh vien (6 ky tu): '))
    ten =input('Nhap ten sinh vien : ')
    diem = float(input('Nhap diem sinh vien : '))
    diem = round(diem)
    ds.append([ma, ten, diem])
ds.sort(key=lambda  sv: sv[2], reverse= True)
print("\n Danh sach sinh vien sau sap xep: ")
for sv in ds:
    print(f"{sv[0]}-{sv[1]}-{sv[2]}")