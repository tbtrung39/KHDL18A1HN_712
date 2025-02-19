import math
a = float(input("Nhập vận tốc a: "))
log4_5 = math.log(5) / math.log(4)
t = (a ** 4) / log4_5
print(f"Thời gian xe dừng lại: {round(t, 2)} giây")