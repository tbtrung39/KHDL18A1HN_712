import math

def is_TamGiac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def ChuviTamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        return None 

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        p = ChuviTamGiac(a, b, c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    else:
        return None 