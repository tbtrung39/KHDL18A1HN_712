def tinh_chu_vi(r):
    return 2 * 3.14 * r

def tinh_dien_tich(r):
    return 3.14 * r * r

r = float(input("Nhập bán kính hình tròn: "))

chu_vi = tinh_chu_vi(r)
dien_tich = tinh_dien_tich(r)

print(f"Chu vi hình tròn là: {chu_vi}")
print(f"Diện tích hình tròn là: {dien_tich}")
