def tim_max(a, b):
    if a > b:
        return a
    else:
        return b

def max_3_so(a, b, c):
    return tim_max(tim_max(a, b), c)
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
so3 = float(input("Nhập số thứ ba: "))

ket_qua = max_3_so(so1, so2, so3)
print("Số lớn nhất là:", ket_qua)
