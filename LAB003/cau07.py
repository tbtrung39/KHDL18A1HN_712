n = int(input("Nhập n: "))
tổng = sum(1 / i for i in range(1, n + 1))
for _ in range(1): 
    print(f"Tổng nghịch đảo của {n} số đầu tiên: {round(tổng, 3)}")
else:
    print("Đã tính xong tổng nghịch đảo!")
