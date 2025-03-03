#BAI9A
n = int(input("Nhập số nguyên dương n: "))  
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n: "))

S4 = 0  
for i in range(1, n + 1):  
    S4 += i ** 2  

print("Tổng S4 =", S4)  

