import math

def tinh_bieu_thuc(x):
    if x < 0:
        return "x không hợp lệ"
    tu = -x + math.sqrt(x)
    mau = 2 + 4 * math.sqrt(x) + (1 / 7)
    return round(tu / mau, 2)

x = float(input("Nhập giá trị x: "))
ket_qua = tinh_bieu_thuc(x)
print(f"Giá trị của biểu thức là: {ket_qua}")
