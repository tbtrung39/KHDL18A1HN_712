#Cau1
#1a
n = int(input("Nhập số nguyên dương n: "))  
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("Tổng S4 =", S4)

#1b
n = int(input("Nhập số nguyên dương n: "))  
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
S5 = 0
i = 1
count = 0  # Đếm số số lẻ
while count < n:
    S5 += i ** 3
    i += 2  # Chỉ lấy số lẻ
    count += 1
print("Tổng S5 =", S5)

#1c
n = int(input("Nhập số nguyên dương n: "))  
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
S6 = 0
i = 2
count = 0  # Đếm số số chẵn
while count < n:
    S6 += i ** 4
    i += 2  # Chỉ lấy số chẵn
    count += 1
print("Tổng S6 =", S6)