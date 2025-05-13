n = int(input("Nhap so luong thi sinh: "))
danh_sach_diem = {}

for _ in range(n):
    sbd = input("So bao danh: ")
    ten = input("Ho ten: ")
    diem = float(input("Diem thi: "))
    danh_sach_diem[sbd] = (ten, diem)

tra_sbd = input("Nhap so bao danh can tra cuu: ")
if tra_sbd in danh_sach_diem:
    print("Ho ten:", danh_sach_diem[tra_sbd][0])
    print("Diem thi:", danh_sach_diem[tra_sbd][1])
else:
    print("Khong tim thay so bao danh.")