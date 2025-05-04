def Ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def Bcnn(a, b):
    return abs(a * b) // Ucln(a, b)
def SumDivisor(n):
    return sum(i for i in range(1, n+1) if n % i == 0)

import sohoc
print(sohoc.Ucln(12, 18))
print(sohoc.Bcnn(12, 18))
print(sohoc.SumDivisor(12))