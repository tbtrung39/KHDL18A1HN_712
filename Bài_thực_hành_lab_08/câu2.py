def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(a, b):
    u = ucln(a, b)
    return a // u, b // u

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu_moi, mau_moi = rut_gon(tu, mau)
print(f"Phân số rút gọn: {tu_moi}/{mau_moi}")
