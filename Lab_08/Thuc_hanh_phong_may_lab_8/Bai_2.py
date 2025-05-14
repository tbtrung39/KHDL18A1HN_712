def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon_phan_so(tu, mau):
    u = ucln(tu, mau)
    return tu // u, mau // u
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
if mau == 0:
    print("Phân số không hợp lệ (mẫu số = 0).")
else:
    tu_moi, mau_moi = rut_gon_phan_so(tu, mau)
    print(f"Phân số rút gọn: {tu_moi}/{mau_moi}")