import modulenguyen

n = int(input("Nhập số phần tử của dãy (tối đa 100): "))
while n > 100 or n <= 0:
    n = int(input("Nhập lại (1-100): "))

day = modulenguyen.tao_day_ngau_nhien(n)
modulenguyen.hien_thi_day(day)
so_nt_7 = modulenguyen.chia_het_cho_7_nguyento(day)
print("Các số nguyên tố chia hết cho 7:", so_nt_7)
tong_le = modulenguyen.tong_so_le(day)
print("Tổng các số lẻ trong dãy:", tong_le)

scp = modulenguyen.so_chinh_phuong(day)
if scp:
    print("Các số chính phương trong dãy:", scp)
else:
    print("Không có số chính phương nào trong dãy.")
