n = int(input("Nhập số hàng của tam giác: "))

# c
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))

print()

#b
for i in range(n):
    if i == 0 or i == n - 1:
        print(" " * (n - i - 1) + "* " * (i + 1))
    else:
        print(" " * (n - i - 1) + "* " + "  " * (i - 1) + "*")

print()
#a
n = int(input("Nhập số hàng của tam giác: "))
for i in range(n):
    if i == n - 1:
        print("* " * (n)) 
    else:
        print(" " * (n - i - 1) + "*", end="")
        if i > 0:
            print(" " * (2 * i - 1) + "*")
        else:
            print()