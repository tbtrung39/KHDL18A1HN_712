while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhạpa số nguyên dương lớn hơn 0!")
#câu a
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("Tổng S4 =", S4)
#câub
S5 = 0 
i = 0
while i < n:
    so_le = 2 * i + 1
    S5 += so_le ** 3
    i += 1
print("Tổng S5 =", S5)
#câuc 
S6 = 0 
i = 1 
while i <= n:
    so_chan = 2* i
    S6 += so_chan ** 4 
    i += 1
print("Tổng S6 =", S6)