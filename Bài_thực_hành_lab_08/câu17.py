from functools import reduce

def tao_list_tu_1_den_n():
    n = int(input("Nhập số nguyên n: "))
    return list(range(1, n + 1))

def tong_so_chan(lst):
    chan = list(filter(lambda x: x % 2 == 0, lst))
    return reduce(lambda a, b: a + b, chan, 0)

lst = tao_list_tu_1_den_n()
tong_chan = tong_so_chan(lst)
print("Tổng các số chẵn là:", tong_chan)
