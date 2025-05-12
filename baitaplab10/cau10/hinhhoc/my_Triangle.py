import math

def is_TamGiac(a, b, c):
    """Kiểm tra 3 số a, b, c có tạo thành tam giác không"""
    return a + b > c and a + c > b and b + c > a

def ChuviTamGiac(a, b, c):
    """Tính chu vi tam giác"""
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        return None  # hoặc có thể raise exception nếu muốn

def S_TamGiac(a, b, c):
    """Tính diện tích tam giác theo công thức Heron"""
    if not is_TamGiac(a, b, c):
        return None
        
    p = ChuviTamGiac(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))