h = int(input("Nhập chiều cao tam giác :"))
k = h*2 
for i in range(1,h+1) : 
    for j in range(1,k+1) : 
        print(end=" ")
    for m in range(1,i+1) : 
        print("*",end=' ')
    k = k-1 
    print()