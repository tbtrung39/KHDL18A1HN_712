import math

def rut_gon_phan_so(tu, mau):
    ucln = math.gcd(tu, mau)
    return tu // ucln, mau // ucln

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_moi, mau_moi = rut_gon_phan_so(tu, mau)
print(f"Phân số rút gọn: {tu_moi}/{mau_moi}")
