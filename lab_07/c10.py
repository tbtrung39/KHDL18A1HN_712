m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))

digits_m = set(str(m))
digits_n = set(str(n))

common_digits = digits_m & digits_n
total = sum(int(d) for d in common_digits)

print("Các chữ số chung:", common_digits)
print("Tổng các chữ số chung:", total)
