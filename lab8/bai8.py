import math

def chu_vi(r):
    return 2 * math.pi * r

def dien_tich(r):
    return math.pi * r ** 2

r = float(input("Nhập bán kính: "))
print("Chu vi:", chu_vi(r))
print("Diện tích:", dien_tich(r))
