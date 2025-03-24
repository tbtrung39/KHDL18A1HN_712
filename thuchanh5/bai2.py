a = input("Nhập chuỗi kí tự ")
dem = 0 
for i in a :
    if not "a" <= i <= "z" and not "0" <= i <= "9" : 
        dem+= 1 
print(f"Có {dem} kí tự không phải là tiếng anh và số trong chuỗi")