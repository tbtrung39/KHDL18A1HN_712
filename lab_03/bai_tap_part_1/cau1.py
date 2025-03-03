n = int(input("Nhập n: "))
S = 1
T = 1
for i in range(1, n+1):
    T = T * (2 * i) / (2 * i + 1)
    S = S + T
print("Kết quả:", round(S, 3))
