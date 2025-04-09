# Cau 17.

from functools import reduce
n = int(input("Nhập n: "))
lst = list(range(1, n + 1))
so_chan = list(filter(lambda x: x % 2 == 0, lst))
tong_chan = reduce(lambda a, b: a + b, so_chan)
print("Danh sách số chẵn:", so_chan)
print("Tổng các số chẵn:", tong_chan)
