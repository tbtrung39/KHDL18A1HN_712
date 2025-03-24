a = input("Nhập văn bản bất kì: ") 
tu = input("Nhập từ muốn tìm: ") 

dem = 0
check = ""
for i in range(len(a)):
    if a[i] != " ":
        check += a[i]  
    else:
        if check == tu:  
            dem += 1
        check = ""  


if check == tu:
    dem += 1

print(f"Số lần xuất hiện của '{tu}' là: {dem}")
