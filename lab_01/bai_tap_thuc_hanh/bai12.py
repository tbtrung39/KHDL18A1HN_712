import math

def tinh_thoi_gian_dung_xe(a):
    log4_5 = math.log(5, 4)  
    t = (a**4) / log4_5
    return round(t, 2)
a = float(input("Nhập vận tốc ban đầu của ô tô (a): "))
thoi_gian = tinh_thoi_gian_dung_xe(a)
print(f"Thời gian ô tô đi được cho đến lúc dừng là: {thoi_gian} giây")
