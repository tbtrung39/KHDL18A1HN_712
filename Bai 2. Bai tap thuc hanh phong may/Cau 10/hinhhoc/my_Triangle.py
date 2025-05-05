import math

def tinh_chu_vi(a, b, c):
    return a + b + c

def tinh_dien_tich(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
