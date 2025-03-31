#Câu 8:
n = int(input("Nhập số phần tử của dãy Fibonacci: "))

fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 1)]

print(", ".join(map(str, fib[:n])))