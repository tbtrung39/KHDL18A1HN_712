n = int(input("Nhập n: "))
primes = []
i = 2
while len(primes) < n:
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
    i += 1

print("Các số nguyên tố đầu tiên:", primes)
