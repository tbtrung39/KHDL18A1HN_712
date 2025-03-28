n = int(input("Nhập bậc của ma trận đơn vị (n): "))
A =[]
for i in range(n):
    row = []
    for j in range(n):
        if i ==j:
            row. append(1)
        else:
            row. append(0)
    A.append(row)
print("\n Ma trân đơn vị bậc {n} là:",n)
for row in A:
    print(row)