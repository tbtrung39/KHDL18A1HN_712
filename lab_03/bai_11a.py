h = int(input("Nhập số dòng của tam giác : "))
for i in range(1, h + 1):
    print(" " * (h - i), end="")

    if i == 1:
        print(" *")
    elif i == h:
        print("* " * (h + 1))
    else:
        print("*", end=" ")
        print("  " * (i - 1), end="")
        print("*")