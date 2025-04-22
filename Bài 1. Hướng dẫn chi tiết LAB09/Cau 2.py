# Cau 2.
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)
n = int(input("Nhap vao so n: "))
result = giai_thua(n)
print("Giai thua cua", n, "la:", result)