n = int(input("Nhập số lần tung 3 xúc xắc: "))
xac_xuat  = 1 - (5/6)**(3 * n)
print(f"Xác suất có ít nhất một lần cả ba xúc xắc ra 6 trong {n} lần tung là: {xac_xuat:.2f}")
