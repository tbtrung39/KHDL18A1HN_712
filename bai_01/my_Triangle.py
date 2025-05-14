# my_Triangle.py

import math

def is_TamGiac(a, b, c):
    """
    Kiểm tra xem ba số a, b, c có tạo thành một tam giác không.

    Args:
        a (float): Độ dài cạnh thứ nhất.
        b (float): Độ dài cạnh thứ hai.
        c (float): Độ dài cạnh thứ ba.

    Returns:
        bool: True nếu a, b, c tạo thành tam giác, False nếu không.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

def ChuviTamGiac(a, b, c):
    """
    Tính chu vi của tam giác với ba cạnh a, b, c.

    Args:
        a (float): Độ dài cạnh thứ nhất.
        b (float): Độ dài cạnh thứ hai.
        c (float): Độ dài cạnh thứ ba.

    Returns:
        float: Chu vi của tam giác.
    """
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        return "Ba cạnh không tạo thành tam giác."

def S_TamGiac(a, b, c):
    """
    Tính diện tích của tam giác với ba cạnh a, b, c (sử dụng công thức Heron).

    Args:
        a (float): Độ dài cạnh thứ nhất.
        b (float): Độ dài cạnh thứ hai.
        c (float): Độ dài cạnh thứ ba.

    Returns:
        float: Diện tích của tam giác.
    """
    if is_TamGiac(a, b, c):
        p = (a + b + c) / 2  # Nửa chu vi
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return "Ba cạnh không tạo thành tam giác."

if __name__ == "__main__":
    # Ví dụ kiểm tra module
    print(f"Kiểm tra (3, 4, 5) có phải là tam giác? {is_TamGiac(3, 4, 5)}")
    print(f"Chu vi tam giác (3, 4, 5): {ChuviTamGiac(3, 4, 5)}")
    print(f"Diện tích tam giác (3, 4, 5): {S_TamGiac(3, 4, 5)}")

    print(f"\nKiểm tra (1, 2, 5) có phải là tam giác? {is_TamGiac(1, 2, 5)}")
    print(f"Chu vi tam giác (1, 2, 5): {ChuviTamGiac(1, 2, 5)}")
    print(f"Diện tích tam giác (1, 2, 5): {S_TamGiac(1, 2, 5)}")