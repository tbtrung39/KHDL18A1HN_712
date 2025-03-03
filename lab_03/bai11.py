# Hình B
n = int(input("Nhập số hàng của tam giác: "))
for i in range(1, n + 1):  
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, 2 * i): 
        if j == 1 or j == 2 * i - 1 or i == n:  
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    
    print() 

# Hình C
h = int(input("Nhập chiều cao tam giác: "))
k = h*2 
for i in range(1,h+1) : 
    for j in range(1,k+1) : 
        print(end=" ")
    for m in range(1,i+1) : 
        print("*",end=' ')
    k = k-1 
    print()




