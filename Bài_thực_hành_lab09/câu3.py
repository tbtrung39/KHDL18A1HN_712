def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))
result = power(a,n)
print("lũy thừa của", a, "mũ", n, "là: ",result)
