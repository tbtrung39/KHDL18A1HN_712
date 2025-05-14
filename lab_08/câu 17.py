from functools import reduce

n = int(input("Nhập số lượng phần tử n: "))
ds = list(map(int, input(f"Nhập {n} số nguyên, cách nhau bằng dấu cách: ").split()))

so_chan = list(filter(lambda x: x % 2 == 0, ds))

tong_chan = reduce(lambda a, b: a + b, so_chan, 0)

print("Tổng các số chẵn trong danh sách là:", tong_chan)
