import math

def tinh_thoi_gian_dung_xe(a):
    """Tính thời gian ô tô dừng."""
    return round(a**4 / math.log(5, 4), 2)

# Ví dụ sử dụng
a = 5  # Giả sử vận tốc ban đầu là 5 m/s
thoi_gian = tinh_thoi_gian_dung_xe(a)
print(f"Thời gian ô tô dừng: {thoi_gian} giây")