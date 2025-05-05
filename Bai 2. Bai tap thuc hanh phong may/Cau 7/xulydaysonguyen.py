import random
import math

def sinh_day_so(n):
    return [random.randint(1, 100) for _ in range(n)]

def so_nguyen_to_chia_het_cho_7(day):
    def la_so_nguyen_to(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    return [x for x in day if la_so_nguyen_to(x) and x % 7 == 0]

def tong_so_le(day):
    return sum(x for x in day if x % 2 == 1)

def so_chinh_phuong(day):
    def la_chinh_phuong(x):
        can = math.isqrt(x)
        return can * can == x
    return [x for x in day if la_chinh_phuong(x)]
