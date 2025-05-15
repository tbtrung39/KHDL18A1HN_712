import random
import math

def tao_day_ngau_nhien(n):
    return [random.randint(1, 1000) for _ in range(n)]

def hien_thi_day(day):
    print("Dãy số:", day)

def chia_het_cho_7_nguyento(day):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in day if x % 7 == 0 and is_prime(x)]

def tong_so_le(day):
    return sum(x for x in day if x % 2 != 0)

def so_chinh_phuong(day):
    cps = [x for x in day if int(math.sqrt(x))**2 == x]
    return cps
