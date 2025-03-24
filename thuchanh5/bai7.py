a = input("Nhập chuỗi : ") 
b = str()
tong = 0 
for i  in a : 
    if "0" <= i <= "9" : 
        b += i 
b = int(b)
for i in range(1,b) : 
    if b % i == 0 : 
        tong += i 
if tong == b : 
    print(f"{b} : Đây là số hoàn hảo ")
else : 
    print(f"{b} : Đây không phải số hoàn hảo ")
