a = float(input("Nhập vận tốc ban đầu của xe (a): "))

# Tính log4(5) (có thể tính trước giá trị này)
log4_5 = 1.160964047443681

# Tính thời gian dừng xe
thoi_gian_dung_xe = a**4 / log4_5

# Làm tròn đến hai chữ số thập phân
thoi_gian_dung_xe_rounded = int(thoi_gian_dung_xe * 100) / 100

# In kết quả
print("Thời gian ô tô đi được cho đến khi dừng là:", thoi_gian_dung_xe_rounded)