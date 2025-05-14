from functools import reduce

n = int(input("Nhập số n: "))

lst = list(range(1, n + 1))
print("Danh sách từ 1 đến n:", lst)

so_chan = list(filter(lambda x: x % 2 == 0, lst))
print("Danh sách số chẵn:", so_chan)

tong_chan = reduce(lambda a, b: a + b, so_chan)
print("Tổng các số chẵn:", tong_chan)
