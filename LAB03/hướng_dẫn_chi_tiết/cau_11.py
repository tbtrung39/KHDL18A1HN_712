n = int(input("Nhập n: "))
s = sum((2 * i + 1) / (2 * i + 3) for i in range(n))  
print(f"Kết quả: {s:.3f}") 