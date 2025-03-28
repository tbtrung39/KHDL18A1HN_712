n = int(input("Nhập số lượng phần tử Fibonacci: "))

# Tạo dãy Fibonacci
fib = [0, 1]
while len(fib) <= n:
    fib.append(fib[-1] + fib[-2])

# In kết quả cách nhau bằng dấu phẩy
print("Dãy Fibonacci:", ", ".join(map(str, fib[:n+1])))