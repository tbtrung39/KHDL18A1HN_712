# Cau 5.

def tinh_S1(n):
    if n == 1:
        return 1
    return n + tinh_S1(n - 1)
def tinh_S2(n):
    if n == 1:
        return 1
    return n**2 + tinh_S2(n - 1)
def nhap_n():
    try:
        n = int(input("Nhap so nguyen duong n: "))
        if n <= 0:
            raise ValueError("n phai la so nguyen duong lon hon 0")
        return n
    except ValueError as e:
        print("Loi:", e)
        return None
def chay_bai_5():
    n = nhap_n()
    if n is None:
        print("Khong the tinh tong vi n khong hop le.")
        return
    try:
        s1 = tinh_S1(n)
        s2 = tinh_S2(n)
        print(f"Tong S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"Tong S2 = 1^2 + 2^2 + ... + {n}^2 = {s2}")
    except RecursionError:
        print("Loi: Qua muc de quy toi da.")
    except Exception as e:
        print("Loi xay ra:", e)
chay_bai_5()
