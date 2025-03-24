c1 = input("Nhập chuỗi 1")
c2 = input("Nhập chuỗi 2 ") 
c3 = str()
i = 0 
check = 0 
if len(c1) > len(c2) : 
    check = len(c1) 
else : 
    check = len(c2) 
while i <= check : 
    if len(c1) > i : 
     c3 += c1[i]
    if len(c2) > i : 
     c3+= c2[i]
    i += 1 
print(c3)
    

