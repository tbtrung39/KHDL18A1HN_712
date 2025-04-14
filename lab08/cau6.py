def tinh_chu_vi_va_dien_tich(r):
    from math import pi
    return (2 * pi * r, pi * r * r)

r = float(input("Nhập bán kính hình tròn: "))
cv, dt = tinh_chu_vi_va_dien_tich(r)
print("Chu vi:", cv)
print("Diện tích:", dt)