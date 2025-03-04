n = int(input("Nhập số nguyên dương n: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")