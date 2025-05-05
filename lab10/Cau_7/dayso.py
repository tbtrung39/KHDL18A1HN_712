import random
import math
def taojdayso(soluong=100):
    return [random.randint(1,1000)for _ in range(soluong)]
def la_nguyen_to(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def chia_7_nt(day):
    return [x for x in day if x%7 ==0 and la_nguyen_to(x)]
def tong_so_le(day):
    return sum(x for x in day if x%2 !=0)
def co_so_chinh_phuong(day):
    for x in day:
        can=int(math.sqrt(x))
        if can*can==x:
            return True
    return False
