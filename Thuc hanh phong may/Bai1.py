import os
filename = 'dayso.dat'
def tong_hang_le(filename):
    tong = 0
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            line = lines[i]
            numbers = map(int, line.strip().split())
            tong += sum(numbers)
    return tong
tong = tong_hang_le(filename)
print("Tổng các số ở hàng lẻ là:", tong)
