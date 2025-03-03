n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương")
else:
    S = 0
    for i in range(1, n + 1):
        S += 1 / i
    
    print(f"Tổng nghịch đảo của {n} số nguyên đầu tiên là: {S}")