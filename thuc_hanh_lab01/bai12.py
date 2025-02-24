import math

t = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))
a = t**4 + (math.log(5, 4))*(-t)

print("Thời gian ô tô đi được cho đến khi dừng lại là:", round(a, 2), "giây")
