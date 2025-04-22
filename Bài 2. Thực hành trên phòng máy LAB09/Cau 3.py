# Cau 3.
def hoan_vi(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            hoan_vi(a, l+1, r)
            a[l], a[i] = a[i], a[l]

n = int(input("Nhap n: "))
a = list(range(1, n + 1))
hoan_vi(a, 0, n-1)