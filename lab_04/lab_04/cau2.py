#Cau2
#2a
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s = s + 1 / i
    i = i + 1
print("Tổng S =", s)

#2b
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s = s + 1 / (i * (i + 1))
    i = i + 1
print("Tổng S =", s)

#2c
import math
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s = s + 1 / math.sqrt(i + 1)
    i = i + 1
print("Tổng S =", s)