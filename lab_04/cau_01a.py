def nhap_so():
    while True:
        n = int(input("Nhập n (số nguyên dương): "))
        if n > 0:
            return n
        else:
            print("Số nhập vào phải là số nguyên dương, vui lòng nhập lại!")
def tinh_s4(n):
    S4 = 0
    i = 1
    while i <= n:
        S4 += i**2
        i += 1
    return S4
n = nhap_so()
S4 = tinh_s4(n)
print(f"Tổng S4 = {S4}")

