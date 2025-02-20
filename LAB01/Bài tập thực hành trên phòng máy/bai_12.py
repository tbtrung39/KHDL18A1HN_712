import math
a = float(input("Nhập vận tốc ban đầu của xe (m/s): "))
log2_5 = math.log2(5)
t = a / (2 * log2_5)
print("Thời gian xe đi cho đến khi dừng lại: %.2f giây" % t)