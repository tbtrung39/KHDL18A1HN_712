n = int(input("Nhập n: "))
for so in range(2, n + 1):
    so_nguyen_to = True
    for i in range(2, so):  
        if so % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(so, end=" ")
