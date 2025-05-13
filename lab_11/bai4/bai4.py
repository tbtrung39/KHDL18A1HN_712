import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = set()
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
    return sorted(factors)

sample_numbers = [12, 18, 20, 45, 77]
with open('f_in.dat', 'w') as fin:
    for num in sample_numbers:
        fin.write(str(num) + '\n')

with open('f_in.dat', 'r') as fin:
    numbers = [int(line.strip()) for line in fin]

with open('f_out.dat', 'w') as fout:
    for num in numbers:
        factors = prime_factors(num)
        fout.write(' '.join(map(str, factors)) + '\n')

print("Đã ghi kết quả vào file f_out.dat!")
