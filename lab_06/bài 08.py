
n = int(input("Nhập số n: "))


fib = [0, 1] + [0] * (n - 1)
[fib.__setitem__(i, fib[i - 1] + fib[i - 2]) for i in range(2, n + 1)]


print(", ".join(map(str, fib)))