def S1(n):
    if n == 0:
        return 1
    return n + S1(n-1)
def S2(n):
    if n == 1:
        return 1
    return n**2 + S2(n-1)
while True:
    try:
        n = int(input("Nhap n: "))
        if not int(n):
            raise ValueError ("Nhap sai kieu du lieu")
        if not n > 0:
            raise Exception ("Nhap so lon hon khong")
        break
    except ValueError as e:
        print(f"Loi: {e}")
    except Exception as a:
        print(f"Loi: {a}")
print(f"Tong S1: {S1(n)}")
print(f"Tong S2: {S2(n)}")