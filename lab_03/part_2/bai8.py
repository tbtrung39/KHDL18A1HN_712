#a
n = int(input("Nhập số nguyên dương n: "))  
S1 = 0  
for i in range(1, n + 1):  
    S1 += i  
print("Tổng S1 =", S1)  

#b
n = int(input("Nhập số nguyên dương n: ")) 
S2 = 0  
for i in range(1, n + 1):  
    S2 += i ** 2  
print("Tổng S2 =", S2)  

#c
n = int(input("Nhập số nguyên dương n: "))
S3 = 0  
for i in range(1, n + 1):  
    S3 += 1 / i  
print("Tổng S3 =", S3) 