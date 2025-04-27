def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

so = int(input("Nhập số nguyên: "))
print("Số sau khi đảo ngược là:", reverse_number(so))
