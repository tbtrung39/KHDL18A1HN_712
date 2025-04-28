#câu 6:
import random
n=int(input("Nhap n:"))
A = list(range(1,n+1))
result = []
while A:
    x = random.choice(A)
    result.append(x)
    A.remove(x)
print("Hoan vi ngau nhien:",result)
