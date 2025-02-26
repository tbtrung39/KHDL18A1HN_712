# Nhập số hàng của tam giác
n = int(input("Nhập số hàng của tam giác: "))

# (b) Tam giác rỗng
print("\n(b) Tam giác rỗng")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)  
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "* ")

