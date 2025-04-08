import math
a = float(input("Nhập vận tốc ban đầu (m/s): "))
log_4_5 = math.log(5) / math.log(4)  # Tính log cơ số 4 của 5
t = a**5 / log_4_5  
t = int(t * 100) / 100  
print("Thời gian ô tô đi cho đến khi dừng lại là:", t, "giây")
