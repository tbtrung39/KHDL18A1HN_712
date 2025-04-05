n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(1, n + 1):
    is_prime = True
    if i < 2:
        is_prime = False
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime and n % i == 0:
        A.add(i)

for i in range(2, n):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i not in A:
        B.add(i)

print("Tập hợp A (ước số nguyên tố của n):", A)
print("Tập hợp B (số nguyên tố nhỏ hơn n và không là ước của n):", B)