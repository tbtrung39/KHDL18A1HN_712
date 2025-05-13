def tong1(n):
    if n == 1:
        return 1
    return n + tong1(n - 1)

def tong2(n):
    if n == 1:
        return 1
    return n**2 + tong2(n - 1)

try:
    n = int(input("Nhap so nguyen duong n: "))
    
    if n <= 0:
        raise ValueError("n phai la so nguyen duong!")

    s1 = tong1(n)
    s2 = tong2(n)

    print(f"S1 = 1 + 2 + ... + {n} = {s1}")
    print(f"S2 = 1^2 + 2^2 + ... + {n}^2 = {s2}")

except ValueError as e:
    print("Loi nhap lieu:", e)
except Exception:
    print("Da xay ra loi khong xac dinh.")
