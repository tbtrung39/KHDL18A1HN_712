import random
import math

def sinh_day():
    return [random.randint(1, 100) for _ in range(10)]

def so_chia_het_cho_7(lst):
    return [x for x in lst if x % 7 == 0]

def tong_so_le(lst):
    return sum(x for x in lst if x % 2 == 1)

def co_so_chinh_phuong(lst):
    squares = [x for x in lst if math.isqrt(x)**2 == x]
    return squares if squares else "Không có số chính phương"
