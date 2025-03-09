n = int(input("Nhập n: "))
#a
s1 = 0
for i in range(1, n+1):
    s1 += (-1)**(i+1) / i
print("Tổng:", s1)

#b
s2 = 0
for i in range(1, n+1):
    s2 += 1 / (i * (i+1))
print("Tổng:", s2)

#c
import math
s3 = 0
for i in range(2, n+2):
    s3 += 1 / math.sqrt(i)
print("Tổng:", s3)