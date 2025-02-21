ngay = int(input("Nhập ngày : "))
thang = int(input("Nhập tháng : "))
if ngay == 30 and thang in (4,6,9,12) : 
    ngay = 1 
    thang += 1 
elif ngay == 31 and thang in (1,3,5,7,8,10,12) : 
    ngay = 1 
    thang+= 1 
elif ngay == 28 and thang == 2 : 
    ngay = 1 
    thang += 1 
else : 
    ngay += 1 
print(f"Ngày tiếp theo là ngày {ngay} tháng {thang} ")