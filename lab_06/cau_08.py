n = int(input("Nhập số lượng phần tử trong dãy Fibonacci: "))
fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, n)]
print(", ".join(map(str, fibonacci)))
