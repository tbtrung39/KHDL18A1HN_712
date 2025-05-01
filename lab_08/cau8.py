import math  

def tinh_chu_vi(r):
    return 2 * math.pi * r

def tinh_dien_tich(r):
    return math.pi * r * r

r = float(input("Nhập bán kính hình tròn: "))

chu_vi = tinh_chu_vi(r)
dien_tich = tinh_dien_tich(r)

print(f"Chu vi hình tròn là: {chu_vi}")
print(f"Diện tích hình tròn là: {dien_tich}")
