import math

def tinh_f_x(x):
    """Tính giá trị biểu thức f(x)."""
    tu = -x + math.sqrt(x**2 + 4)
    mau = 7 * math.sqrt(x**4 + 1)
    return round(tu / mau, 2)

# Ví dụ sử dụng
x = 2
print(f"f({x}) = {tinh_f_x(x)}")