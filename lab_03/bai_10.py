n = int(input("Nhập vào một số nguyên dương: "))
i = 2  
while i <= n:
    if n % i == 0:
        print(i, end=" ")  
        n = n // i  
    else:
        i += 1  
print(f"Phân tích thừa số nguyên tố của",n, end="")
