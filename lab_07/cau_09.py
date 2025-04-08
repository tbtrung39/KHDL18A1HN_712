n = int(input("Nhập n: "))
A = set()
B = set()

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return False
    return True

for i in range(1, n+1):
    if n % i == 0 and is_prime(i):
        A.add(i)

for i in range(2, n):
    if is_prime(i) and n % i != 0:
        B.add(i)

print("Tập A (ước là số nguyên tố):", A)
print("Tập B (nguyên tố < n, không phải ước):", B)
