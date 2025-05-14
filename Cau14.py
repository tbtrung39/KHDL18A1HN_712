# Câu 14. Tìm tất cả các số Fibonacci nhỏ hơn N mà cũng là số nguyên tố.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_fibonacci_nho_hon_n(N):
    fib = [0, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib >= N:
            break
        fib.append(next_fib)
    return [x for x in fib if la_so_nguyen_to(x)]
N = int(input())
result = so_fibonacci_nho_hon_n(N)
print(f"Các số Fibonacci nhỏ hơn {N} và là số nguyên tố: {result}")
