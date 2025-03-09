def nhap_so():
    while True:
        n = int(input("Nhập n (số nguyên dương): "))
        if n > 0:
            return n
        else:
            print("Số nhập vào phải là số nguyên dương, vui lòng nhập lại!")
def tinh_s5(n):
    S5 = 0
    i = 1
    while i <= n:
        S5 += (2*i + 1)**3
        i += 1
    return S5
n = nhap_so()
S5 = tinh_s5(n)
print(f"Tổng S5 = {S5}")
