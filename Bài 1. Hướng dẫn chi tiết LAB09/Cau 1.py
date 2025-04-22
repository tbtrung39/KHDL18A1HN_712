# Cau 1.
def cap_so_nhan(n):
    if n == 1:
        return 7
    else:
        return 2 * cap_so_nhan(n-1)

n =   int(input("Nhap vao so n: "))
result = cap_so_nhan(n)
print("So hang thu", n, "cua cap so nhan la:", result)