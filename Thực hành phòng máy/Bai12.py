import math
# Nhập vận tốc ban đầu a
a = float(input("Nhập vận tốc a: "))
# Tính thời gian t khi v(t) = 0
t = (a**4) / math.log(5, 4)
print("Thời gian ô tô đi được cho đến khi dừng là:", round(t,2))