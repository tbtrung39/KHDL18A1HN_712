# b:
def tinh_tong_b(n):
    tong = 0
    for i in range(2, n+1):
        tong += 1 / (i * (i + 1))
    return tong

def main_b():
    n = int(input("Nhập số phần tử n cho biểu thức b): "))
    ket_qua = tinh_tong_b(n)
    print(f"Tổng S của biểu thức b với n = {n} là: {ket_qua}")
main_b()