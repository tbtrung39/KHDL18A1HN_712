import math

def tinh_thoi_gian_dung(a):
    t = 0
    while a > 0:
        t += 0.01  # Lấy từng bước nhỏ để tìm thời gian gần đúng
        a = a - t * math.log(4, 5) + (a / 4)
    return round(t, 2)

a = float(input("Nhập vận tốc ban đầu của ô tô: "))
thoi_gian_dung = tinh_thoi_gian_dung(a)
print(f"Thời gian ô tô đi được cho đến lúc dừng: {thoi_gian_dung} giây")
