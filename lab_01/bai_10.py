import math

def tinh_bieu_thuc(x):
    if x <= 0 or x == 1:
        return "x không hợp lệ"
    log4_x = math.log(x) / math.log(4)
    logx_2 = math.log(2) / math.log(x)
    return round(log4_x + logx_2, 2)

x = float(input("Nhập x: "))
ket_qua = tinh_bieu_thuc(x)
print(f"Giá trị của biểu thức là: {ket_qua}")
