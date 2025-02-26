# Nhập số hàng từ người dùng
n = int(input("Nhập số hàng của tam giác: "))

# In hình tam giác (c)
print("\nHình tam giác (c):")
for i in range(n):
    # In khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    # In dấu sao
    for k in range(i + 1):
        print("* ", end="")
    print()  