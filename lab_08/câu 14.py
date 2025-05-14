n = int(input("Nhập số phần tử: "))
lst = list(map(int, input("Nhập các số nguyên: ").split()))
bp = list(map(lambda x: x**2, lst))
print("Bình phương các phần tử:", bp)
