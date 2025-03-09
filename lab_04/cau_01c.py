def nhap_so():
    while True:
        n = int(input("Nhập n (số nguyên dương): "))
        if n > 0:
            return n
        else:
            print("Số nhập vào phải là số nguyên dương, vui lòng nhập lại!")
def tinh_s6(n):
    S6 = 0
    i = 1
    while i <= n:
        S6 += (2*i)**2
        i += 1
    return S6
n = nhap_so()
S6 = tinh_s6(n)
print(f"Tổng S6 = {S6}")
