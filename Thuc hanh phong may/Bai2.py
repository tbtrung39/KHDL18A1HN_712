def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon_phan_so(tu, mau):
    if mau == 0:
        return "Phân số không hợp lệ (mẫu số bằng 0)"
    u = ucln(tu, mau)
    return tu // u, mau // u
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_moi, mau_moi = rut_gon_phan_so(tu, mau)
print(f"Phân số rút gọn: {tu_moi}/{mau_moi}")
