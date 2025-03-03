n = float(input("Nhập số n: "))
if n == int(n):
    print(int(n), "là số nguyên")
else:
    print(n, "không phải số nguyên, số gần nhất là", round(n))