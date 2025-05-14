str = input("Nhập chuỗi nhị phân: ")
n = 0

for i in range(len(str)):
    bit = int(str[i])  
    n = n * 2 + bit  

print(f"Số thập phân là: {n}")
