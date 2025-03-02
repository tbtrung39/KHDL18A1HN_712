h=int(input("Nhập giá trị chiều cao tam giác cân: "))
k = h*2
for i in range(1,h+1) : 
    for j in range(1,k+1) : 
        print(end=" ")
    if i == 1 : 
        print("*",end =" ")
    else : 
        if i == h : 
            for u in range(1,h+1) : 
                print("*",end=" ")
        else :
            print("*",end ="")
            for m in range(1,i*2-2) : 
                print(end=" ") 
            print("*",end ="")
        
    k=k-1
    print()
