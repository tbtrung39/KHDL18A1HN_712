# Câu 11.
# Nhập số hàng của tam giác
n = int(input("Nhập số hàng của tam giác: "))

# a. Vẽ tam giác cân rỗng
print("Tam giác cân rỗng:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i) 
    else:
        print(" " * (n - i) + "* " + " " * (2 * i - 3) + "*")  
print("\n")

# b. Vẽ tam giác đều rỗng
print("Tam giác đều rỗng:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)  
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "*")  
print("\n")

# c. Vẽ tam giác đều đặc
print("Tam giác đều đặc:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
print("\n")
