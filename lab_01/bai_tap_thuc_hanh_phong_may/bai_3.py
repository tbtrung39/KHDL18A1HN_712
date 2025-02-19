r = float(input("Nhập bán kính đáy: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14

s_xq = 2 * pi * r * h
s_tp = s_xq + 2 * pi * r ** 2
v = pi * r ** 2 * h

print(f"Diện tích xung quanh: {s_xq:.2f}")
print(f"Diện tích toàn phần: {s_tp:.2f}")
print(f"Thể tích khối trụ: {v:.2f}")
