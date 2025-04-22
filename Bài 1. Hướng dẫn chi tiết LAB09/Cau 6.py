 # Cau 6.
# a.
def sum_1_to_n(n):
    if n == 1:
        return 1
    else:
        return n +sum_1_to_n(n-1)
n = int(input("Nhap so tu nhien N: "))
result = sum_1_to_n(n)
print("Tong S1 =  1 + 2 + ... + n =", result)

# b.
def sum_even_numbers(n):
    if  n == 1:
        return 2
    else:
        return 2 * n + sum_even_numbers(n-1)
n = int(input("Nhap so tu nhien N: "))
result = sum_even_numbers(n)
print("Tong S2 = 2 + 4 + ... + 2n =", result)

# c.
def sum_odd_numbers(n):
    if n == 1:
        return 1
    else:
        return 2 * n - 1 + sum_odd_numbers(n-1)
n = int(input("Nhap so tu nhien N: "))
result = sum_odd_numbers(n)
print("Tong S3 = 1 + 3 + 5 + ... + 2n-1 =",result)