n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (phải là số nguyên dương): "))
    
S5 = 0
for i in range(n):
    S5 += (2 * i + 1) ** 3
print("S5 =", S5)
