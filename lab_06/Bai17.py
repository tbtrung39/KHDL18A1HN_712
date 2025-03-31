n=int(input("Nhap so n: "))
a=[]
for i in range(n):
    row=[]
    for j in range(n):
        if i==j:
            row.append(1)
        else:
            row.append(0)
    a.append(row)
for row in a:
    print(row)