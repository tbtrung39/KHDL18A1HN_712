import math
n = int(input("Nhập giá trị n: "))
result = 1  
for i in range(1, n + 1):
    result *= (2 * i + 1) / (2 * i + 3)  
print("Kết quả:", round(result, 3))  
