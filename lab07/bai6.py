def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số tự nhiên n: "))
primes = set()
num = 2

while len(primes) < n:
    if is_prime(num):
        primes.add(num)
    num += 1

print(f"Dãy {n} số nguyên tố đầu tiên:", sorted(primes))
