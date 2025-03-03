n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S = S + i**3
print("Tổng lập phương của", n, "số đầu tiên là:", S)