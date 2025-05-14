import math

def calculate_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Các cạnh phải lớn hơn 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Các cạnh không thỏa mãn điều kiện tồn tại tam giác.")
    
    s = (a + b + c) / 2  # Chu vi nửa
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    
    area = calculate_area(a, b, c)
    print(f"Diện tích tam giác là: {area}")
except ValueError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
