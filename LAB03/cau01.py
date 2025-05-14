n = int(input("Nhập n: "))
tổng = 1  
tích = 1  

for i in range(1, n + 1):
    tích *= (2 * i) / (2 * i + 1)  
    tổng += tích  
else:
    print(f"Kết quả: {round(tổng, 3)}") 
