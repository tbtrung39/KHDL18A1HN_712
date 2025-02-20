print("Chương trình tính diện tính xung quanh , diện tích toàn phần , thể tích")
r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))
pi = 3.14
S_xq = 2 * pi * r * h
S_tp = S_xq + 2 * pi * r**2
V = pi * r**2 * h
print("Diện tích xung quanh: ",S_xq)
print("Diện tích toàn phần: ",S_tp)
print("Thể tích khối trụ: ",V)
