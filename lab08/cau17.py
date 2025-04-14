from functools import reduce

def tong_so_chan(lst):
    chan = list(filter(lambda x: x % 2 == 0, lst))
    return reduce(lambda a, b: a + b, chan, 0)

lst = [int(input("Nhập số: ")) for _ in range(int(input("Nhập số lượng phần tử: ")))]
print("Tổng các số chẵn:", tong_so_chan(lst))