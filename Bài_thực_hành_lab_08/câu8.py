import math

def chu_vi(r):
    return 2 * math.pi * r

def dien_tich(r):
    return math.pi * r * r

r = float(input("Nhập bán kính hình tròn: "))
print("Chu vi hình tròn là:", chu_vi(r))
print("Diện tích hình tròn là:", dien_tich(r))
