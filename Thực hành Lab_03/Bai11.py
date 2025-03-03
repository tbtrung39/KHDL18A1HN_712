# Nhập số hàng của tam giác
n = int(input("Nhập số hàng của tam giác: "))
for _ in range(1000):
    if n > 0:
        break
    n = int(input("Vui lòng nhập lại số hàng: "))
# (a)
print("Tam giác (a):")
for i in range(1, n + 1):
    print("* " * i)
# (b)
print("\nTam giác (b):")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# (c)
print("\nTam giác (c):")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("*" + " " * (2 * i - 3) + "*")
