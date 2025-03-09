# a:
def tinh_tong_a(n):
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 1:  
            tong += 1/i
        else:  
            tong -= 1/i
    return tong
def main_a():
    n = int(input("Nhập số phần tử n cho biểu thức a): "))
    ket_qua = tinh_tong_a(n)
    print(f"Tổng S của biểu thức a với n = {n} là: {ket_qua}")
main_a()














