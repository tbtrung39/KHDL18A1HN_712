import random
import math

def sinh_day_so(n=100):
    so_luong = min(n, 100)
    day_so = [random.randint(1, 999) for _ in range(so_luong)]
    print(f"Dãy số ngẫu nhiên ({so_luong} số):")
    print(day_so)
    return day_so

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nt_chia_het_cho_7(day_so):
    ket_qua = [x for x in day_so if x % 7 == 0 and la_so_nguyen_to(x)]
    print("Các số nguyên tố chia hết cho 7:")
    print(ket_qua if ket_qua else "Không có")
    return ket_qua

def tong_so_le(day_so):
    tong = sum(x for x in day_so if x % 2 == 1)
    print(f"Tổng các số lẻ trong dãy là: {tong}")
    return tong

def kiem_tra_so_chinh_phuong(day_so):
    chinh_phuong = [x for x in day_so if int(math.sqrt(x)) ** 2 == x]
    if chinh_phuong:
        print("Các số chính phương trong dãy:")
        print(chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")
    return chinh_phuong