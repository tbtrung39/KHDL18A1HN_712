thang = int(input("Nhap thang: "))
if ( thang in (1,3,5,7,8,10,12)) : 
    print(f"Tháng {thang} có 31 ngày ")
elif ( thang in (4,6,9,11)) : 
    print(f"Tháng {thang} có 30 ngày")
elif thang == 2 : 
    print("Tháng có 28 hoặc 29 ngày") 
else : 
    print("Nhập sai vui lòng nhập lại")