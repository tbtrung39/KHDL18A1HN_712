def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

n = int(input("Nhập số cần đảo ngược: "))
print("Số sau khi đảo ngược:", reverse_number(n))
