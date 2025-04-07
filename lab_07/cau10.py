m = input("Nhập số tự nhiên m: ")
n = input("Nhập số tự nhiên n: ")

common_digits = set(m) & set(n)  # Tìm các chữ số chung
total = sum(int(digit) for digit in common_digits)
print("Tổng các chữ số chung:", total)