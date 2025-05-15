def tinh_S1(n):
    if n==1:
        return 1
    return n+tinh_S1(n-1)
def tinh_S2(n):
    if n==1:
        return 1
    return n**2 + tinh_S2(n-1)
def nhap_so_nguyen_duong():
    while True:
        try:
            n=int(input("Nhập số nguyên dương n:"))
            if n<=0:
                raise ValueError("n phải là số nguyên dương lớn hơn 0")
            return n
        except ValueError as e:
            print(f'lỗi:{e}')
n=nhap_so_nguyen_duong()
tong_S1=tinh_S1(n)
tong_S2=tinh_S2(n)
print(f"S1=1+2+...+{n}={tong_S1}")
print(f"S2=1^2+2^2+...+{n}^2={tong_S2}")