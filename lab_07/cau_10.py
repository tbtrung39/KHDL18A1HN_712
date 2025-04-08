m = input("Nhập m: ")
n = input("Nhập n: ")

common = set(m) & set(n)             
digits = {int(ch) for ch in common if ch.isdigit()}
print("Tổng các chữ số chung:", sum(digits))
