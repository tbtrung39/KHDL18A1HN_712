import math
def tinh_fx_b10(x):
    ket_qua = math.log(x, 4) + math.log(2, x)
    return round(ket_qua, 2)
x = float(input("Nhập giá trị của x: "))