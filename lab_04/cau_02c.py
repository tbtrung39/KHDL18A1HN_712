


#c:
import math
def tinh_tong_c(n):
    tong = 0
    for i in range(2, n+1):
        tong += 1 / math.sqrt(i)
    return tong
def main_c():
    n = int(input("Nhập số phần tử n cho biểu thức c): "))
    ket_qua = tinh_tong_c(n)
    print(f"Tổng S của biểu thức c với n = {n} là: {ket_qua}")
main_c()
