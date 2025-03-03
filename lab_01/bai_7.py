def tim_dinh_parabol(a, b, c):
    """Tìm đỉnh của phương trình bậc 2."""
    x = -b / (2 * a)
    y = a * x**2 + b * x + c
    return round(x, 2), round(y, 2)

# Ví dụ sử dụng
x, y = tim_dinh_parabol(1, -4, 3)
print(f"Đỉnh parabol: ({x}, {y})")