r = float(input("Nhập bán kính đáy của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
pi = 3.14
s_xung_quanh = 2 * pi * r * h
s_toan_phan = 2 * pi * r * (r + h)
V = pi * r**2 * h
print(f"Diện tích xung quanh khối trụ: {s_xung_quanh:.2f}")
print(f"Diện tích toàn phần khối trụ: {s_toan_phan:.2f}")
print(f"Thể tích khối trụ: {V:.2f}")
