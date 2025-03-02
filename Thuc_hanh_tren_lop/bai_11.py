# Nhập số hàng của tam giác
n = int(input("Nhập số hàng của tam giác: "))

# (a) Tam giác trái
print("(a)")
for i in range(1, n+1):
    print("* " * i)

# (b) Tam giác phải
print("\n(b)")
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)

# (c) Tam giác cân
print("\n(c)")
for i in range(n):
    print(" " * (n - i - 1) + "* " * (2 * i + 1))