import math
a = float(input("Nhập vận tốc a của xe ô tô (m/s): "))
log4_5 = math.log(5)/math.log(4)
t = (a ** 4)/log4_5
print(f"Thời gian ô tô dừng lại là: {round(t,2)} giây")