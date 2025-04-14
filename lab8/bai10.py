def uoc_so(n):
    return [i for i in range(1, n+1) if n % i == 0]

n = int(input("Nhập số nguyên dương: "))
print("Các ước của", n, "là:", uoc_so(n))
