#BAI10
n = int(input("Nhập số nguyên dương: "))  
i = 2  
result = ""

while n > 1:  
    count = 0  
    while n % i == 0:  
        n //= i  
        count += 1  
    if count > 0:  
        result += f"{i}^{count} * "  
    i += 1  

print("Phân tích thừa số nguyên tố:", result[:-3])  
