n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / i
print("Tổng nghịch đảo là: %0.2f" % S)