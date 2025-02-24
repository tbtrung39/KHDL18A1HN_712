print("Chương trình xác định chữ số hàng trăm")
n = int(input("Nhập số nguyên: "))
if n < 0:
    n = -n
if n >= 100:
    print(n // 100 % 10)
else:
    print(0)