def Ucln(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def Bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // Ucln(a, b)

def SumDivisors(n):
    if n == 0:
        return 0
    total = 1 if n != 1 else 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total