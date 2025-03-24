a = input("Nhập chuỗi: ")
max_sub = ""  
current_sub = a[0]  
for i in range(1, len(a)):  
    if a[i] == a[i-1]:  
        current_sub += a[i]  
    else:
        if len(current_sub) > len(max_sub):  
            max_sub = current_sub
        current_sub = a[i]  
if len(current_sub) > len(max_sub):
    max_sub = current_sub

print("Chuỗi con dài nhất gồm các ký tự giống nhau:", max_sub)



     
