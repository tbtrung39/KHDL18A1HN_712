import math
def time_to_stop(a):
 log4_5 = math.log(5) / math.log(4) # Tính log cơ số 4 của 5
 t = (a ** 4) / log4_5
 return round(t, 2)
a = float(input("Nhập vận tốc ban đầu a: "))
print(f"Thời gian ô tô đi đến lúc dừng: {time_to_stop(a)} giây")