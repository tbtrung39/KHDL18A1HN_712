import math

def is_TamGiac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def ChuViTamGiac(a, b, c):
    if not is_TamGiac(a, b, c):
        return None
    return a + b + c

def S_TamGiac(a, b, c):
    if not is_TamGiac(a, b, c):
        return None
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
