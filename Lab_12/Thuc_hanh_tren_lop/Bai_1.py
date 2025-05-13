import math

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

try:
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Canh phai > 0")

    if not la_tam_giac(a, b, c):
        raise ValueError("Khong phai tam giac")

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Dien tich tam giac: {s:.2f}")

except ValueError as e:
    print("Loi:", e)
except:
    print("Loi khong xac dinh")
