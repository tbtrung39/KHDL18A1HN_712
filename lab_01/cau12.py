import math
a = float(input("Nhập vận tốc ban đầu của ô tô: "))
log4_5 = math.log(5, 4)  # log_4(5)
t = a**4 / log4_5
print("Thời gian ô tô đi được đến khi dừng lại:", round(t, 2), "giây")