m = input("Nhập số m: ")
n = input("Nhập số n: ")

set_m = set(m)
set_n = set(n)

common_digits = set_m.intersection(set_n)

total_sum = sum(int(digit) for digit in common_digits)

print("Tổng các chữ số chung:", total_sum)
