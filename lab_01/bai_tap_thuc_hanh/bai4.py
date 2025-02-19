import math
def tinh_fx(x):
    tu_so = -x + math.sqrt(x**2 + 4)
    mau_so = 7 * x**4 + 1
    ket_qua = tu_so / mau_so
    return round(ket_qua, 2)
x = float(input("Nhập giá trị x: "))
ket_qua = tinh_fx(x)
print(f"Giá trị của f(x) = {ket_qua}")
