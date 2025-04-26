def uoc_so(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')

n = int(input("Nhập số nguyên dương n: "))
print(f"Các ước số của {n} là:")
uoc_so(n)
