import math

def sinh_day_so():
    return list(range(1, 101))

def liet_ke_chia_het_cho_7():
    return [x for x in range(1, 101) if x % 7 == 0]

def tong_chia_het_7():
    return sum(liet_ke_chia_het_cho_7())

def la_so_chinh_phuong(n):
    return int(n**0.5)**2 == n

def kiem_tra_chinh_phuong():
    return [x for x in range(1, 101) if la_so_chinh_phuong(x)]