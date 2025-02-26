# Nhập số hàng của tam giác
n = int(input("Nhập số hàng của tam giác: "))

# a. Vẽ tam giác cân rỗng
print("Tam giác cân rỗng:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i) 
    else:
        print(" " * (n - i) + "* " + " " * (2 * i - 4) + "*")  
print("\n")

