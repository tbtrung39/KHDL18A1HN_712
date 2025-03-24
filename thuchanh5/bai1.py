a = input("Nhập chuỗi kí tự : ") 
dem = 0 
for i in a : 
    if "0" <= i <= "9" : 
        dem += 1 
print(f"Có {dem} kí tự là số trong chuỗi ")
