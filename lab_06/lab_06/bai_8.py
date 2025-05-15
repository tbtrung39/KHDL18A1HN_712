# Câu 8
n = int(input("Nhap gia tri cua n: "))
fib_list = [0, 1]
[fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(2, n)]
print(" ".join(map(str, fib_list[:n])))