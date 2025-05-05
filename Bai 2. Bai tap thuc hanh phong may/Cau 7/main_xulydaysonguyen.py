import xulydaysonguyen

n = int(input("Nhap so luong phan tu cua day (toi da 100): "))
if n > 100:
    n = 100

day = xulydaysonguyen.sinh_day_so(n)
print("Day so ngau nhien:", day)

so_nguyen_to_7 = xulydaysonguyen.so_nguyen_to_chia_het_cho_7(day)
print("Cac so nguyen to chia het cho 7:", so_nguyen_to_7)

tong_le = xulydaysonguyen.tong_so_le(day)
print("Tong cac so le:", tong_le)

chinh_phuong = xulydaysonguyen.so_chinh_phuong(day)
if chinh_phuong:
    print("Cac so chinh phuong co trong day:", chinh_phuong)
else:
    print("Khong co so chinh phuong trong day.")
